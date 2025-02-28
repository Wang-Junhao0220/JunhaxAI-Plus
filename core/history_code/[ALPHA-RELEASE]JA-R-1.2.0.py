# 优化太多，欢迎测试Bug。
# Bug反馈：https://github.com/Wang-Junhao0220/JunhaxAI/issues?q=is%3Aissue

import re
import os
import glob
import time
import json
import jieba
import openai
from enum import Enum
from typing import List, Dict, Tuple, Optional
from datetime import datetime
from dataclasses import dataclass, field
from collections import Counter


# ================= 配置类 =================
class SummaryMethod(Enum):
    FIRST_QUESTION = 1
    KEYWORDS = 2
    AI_SUMMARY = 3


@dataclass
class APIConfig:
    api_key: str = "sk-61964d0f1b37434496e085fb65dce36d"
    base_url: str = "https://api.deepseek.com"
    # model: str = "gemini-1.5-flash-latest" # gpt-4o-mini
    model: str = "deepseek-chat"
    max_history: int = 300
    save_folder: str = "chat_history"
    timeout: int = 300
    stream_delay: float = 0.1
    system_message: str = "你是一个智能助手，请使用简洁的，用户的输入语言进行交流，回答长度不超过1000字且不允许使用Markdown格式"
    auto_summary_length: int = 30
    max_filename_length: int = 50
    summary_method: SummaryMethod = SummaryMethod.FIRST_QUESTION
    jieba_cache: dict = field(default_factory=dict)
    config_path: str = "ai_config.json"
    auto_save_config: bool = True  # 配置自动保存
    auto_save_chat: bool = True  # 聊天自动保存
    last_config_save: bool = False  # 上次操作是否为配置保存
    last_chat_save: bool = False  # 上次操作是否为聊天保存


API_CONFIG = APIConfig()


# ================= 配置持久化 =================
def save_config():
    """保存配置到本地文件"""
    config_data = {
        "version": 2.1,
        "auto_save_config": API_CONFIG.auto_save_config,
        "auto_save_chat": API_CONFIG.auto_save_chat,
        "summary_method": API_CONFIG.summary_method.value,
        "last_modified": datetime.now().isoformat()
    }
    try:
        with open(API_CONFIG.config_path, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2)
    except Exception as e:
        print(f"⚠️ 配置保存失败: {str(e)}")


def load_config():
    """从本地文件加载配置（带版本兼容）"""
    if not os.path.exists(API_CONFIG.config_path):
        return

    try:
        with open(API_CONFIG.config_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)

            # 处理旧版本配置
            if "version" not in config_data:
                legacy_auto_save = config_data.get("auto_save", True)
                API_CONFIG.auto_save_config = legacy_auto_save
                API_CONFIG.auto_save_chat = legacy_auto_save
            else:
                API_CONFIG.auto_save_config = config_data.get("auto_save_config", True)
                API_CONFIG.auto_save_chat = config_data.get("auto_save_chat", True)

            API_CONFIG.summary_method = SummaryMethod(config_data.get("summary_method", 1))
    except Exception as e:
        print(f"⚠️ 配置加载失败: {str(e)}")


# ================= 工具函数 =================
def sanitize_filename(text: str) -> str:
    """清理文件名中的非法字符并处理空格"""
    cleaned = re.sub(
        r'[\\/*?:"<>|\s]',
        lambda m: '_' if m.group().isspace() else '',
        text
    )
    return cleaned.strip('_')[:API_CONFIG.max_filename_length]


def generate_ai_summary(text: str) -> str:
    """使用AI生成摘要"""
    try:
        client = openai.OpenAI(
            api_key=API_CONFIG.api_key,
            base_url=API_CONFIG.base_url
        )
        response = client.chat.completions.create(
            model=API_CONFIG.model,
            messages=[{
                "role": "system",
                "content": "请用5-8个中文关键词概括以下内容，用下划线连接。示例：深度学习_模型训练_数据增强"
            }, {
                "role": "user",
                "content": text[:2000]
            }],
            max_tokens=50,
            temperature=1.3
        )
        return sanitize_filename(response.choices[0].message.content.strip())
    except Exception as e:
        print(f"AI智能摘要失败: {str(e)}")
        return ""


def generate_summary(history: List[Dict[str, str]]) -> str:
    """安全摘要生成（修复首问提取逻辑）"""
    try:
        if API_CONFIG.summary_method == SummaryMethod.FIRST_QUESTION:
            # 跳过系统消息查找首问
            filtered_history = [msg for msg in history if msg["role"] != "system"]
            first_question = next(
                (msg["content"] for msg in filtered_history if msg["role"] == "user"),
                ""
            )
            if len(first_question) >= 5:
                summary = first_question[:API_CONFIG.auto_summary_length]
            else:
                summary = ""
        elif API_CONFIG.summary_method == SummaryMethod.KEYWORDS:
            contents = [msg["content"] for msg in history if msg["role"] != "system"]
            text = " ".join(contents)
            cache_key = hash(text)
            if cache_key not in API_CONFIG.jieba_cache:
                words = [word for word in jieba.cut(text) if len(word) > 1]
                API_CONFIG.jieba_cache[cache_key] = Counter(words).most_common(3)
            keywords = API_CONFIG.jieba_cache[cache_key]
            summary = "_".join([word for word, _ in keywords]) or "未命名对话"
        elif API_CONFIG.summary_method == SummaryMethod.AI_SUMMARY:
            contents = [msg["content"] for msg in history if msg["role"] != "system"]
            text = " ".join(contents)
            summary = generate_ai_summary(text) or "AI摘要生成失败"
        else:
            summary = ""
    except Exception as e:
        print(f"摘要生成失败: {str(e)}")
        summary = datetime.now().strftime("对话%H%M%S")

    return sanitize_filename(summary) if summary else "未命名对话"


def generate_filename(history: List[Dict[str, str]]) -> str:
    """生成带摘要的文件名（包含chat_前缀）"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary = generate_summary(history)
    return f"chat_{timestamp}_{summary}".strip("_")


def trim_history(history: List[Dict[str, str]], max_length: int) -> List[Dict[str, str]]:
    """安全修剪对话历史"""
    if max_length <= 0:
        return history[:1]

    if len(history) <= 1:
        return history

    keep_pairs = max(max_length * 2, 2)
    return [history[0]] + history[-keep_pairs:]


# ================= 文件操作 =================
def ensure_save_folder() -> None:
    """确保保存目录存在"""
    os.makedirs(API_CONFIG.save_folder, exist_ok=True)


def get_latest_file() -> Optional[str]:
    """获取最新的历史文件（增强过滤）"""
    files = [f for f in glob.glob(os.path.join(API_CONFIG.save_folder, "*.json"))
             if os.path.isfile(f)]
    return max(files, key=os.path.getmtime) if files else None


def parse_save_args(args: List[str], history: List[Dict[str, str]]) -> Tuple[str, str]:
    """安全参数解析"""
    format, filename = "json", None
    valid_formats = ["json", "txt"]

    for arg in args:
        if arg in valid_formats:
            format = arg
        elif not filename:
            clean_arg = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5_-]', '', arg)
            filename = clean_arg[:30]

    filename = filename or generate_filename(history)
    return format, filename


def save_conversation(history: List[Dict[str, str]], args: List[str]) -> str:
    """带预览的保存功能"""
    ensure_save_folder()
    format, filename = parse_save_args(args, history)

    try:
        filepath = os.path.join(API_CONFIG.save_folder, f"{filename}.{format}")
        print(f"即将保存到：{os.path.basename(filepath)}")

        with open(filepath, 'w', encoding='utf-8') as f:
            if format == "json":
                json.dump(history, f, ensure_ascii=False, indent=2)
            else:
                for msg in history:
                    f.write(f"{msg['role']}: {msg['content']}\n\n")
        API_CONFIG.last_chat_save = True  # 标记聊天保存
        return f"✅ 聊天保存成功：{os.path.basename(filepath)}"
    except Exception as e:
        return f"❌ 聊天保存失败: {str(e)}"


def load_conversation(args: List[str]) -> Tuple[Optional[List[Dict[str, str]]], str]:
    """增强版加载对话历史"""
    ensure_save_folder()
    try:
        if not args:
            latest = get_latest_file()
            if not latest:
                return None, "找不到历史文件"
            filename = os.path.basename(latest)[:-5]
        else:
            filename = os.path.basename(args[0]).split('.')[0]

        filepath = os.path.join(API_CONFIG.save_folder, f"{filename}.json")

        if not os.path.exists(filepath):
            available_files = "\n".join([f.stem for f in os.scandir(API_CONFIG.save_folder) if f.is_file()])
            return None, f"文件不存在，可用文件：\n{available_files}"

        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f), f"成功加载: {filename}"
    except json.JSONDecodeError:
        return None, "文件格式错误，无法解析"
    except Exception as e:
        return None, f"加载失败: {str(e)}"


# ================= 命令处理 =================
class StreamPrinter:
    @staticmethod
    def print_stream(response) -> str:
        """处理流式输出（修复索引越界错误）"""
        full_content = []
        print("\r🤖AI助手：", end='', flush=True)

        try:
            for chunk in response:
                time.sleep(API_CONFIG.stream_delay)

                if not hasattr(chunk, 'choices'):
                    continue
                if len(chunk.choices) == 0:
                    continue
                if not hasattr(chunk.choices[0].delta, 'content'):
                    continue

                content = chunk.choices[0].delta.content
                if content:
                    print(content, end='', flush=True)
                    full_content.append(content)
        except Exception as e:
            print(f"\n流式输出中断: {str(e)}")
        finally:
            print()
        return "".join(full_content)


def handle_autosave_command(parts: List[str]) -> str:
    """增强版自动保存命令"""
    if not parts or parts[0].lower() == "all":
        return (
            "🔄 自动保存状态:\n"
            f"• 配置自动保存: {'✅ 开启' if API_CONFIG.auto_save_config else '⚠️ 关闭'}\n"
            f"• 聊天自动保存: {'✅ 开启' if API_CONFIG.auto_save_chat else '⚠️ 关闭'}\n"
            "使用 /autosave [config|chat] [on|off|view] 管理"
        )

    target = parts[0].lower()
    if target not in ("config", "chat"):
        return "❌ 无效目标，请输入 config 或 chat"

    # 查看状态
    if len(parts) == 1 or (len(parts) > 1 and parts[1].lower() == "view"):
        status = API_CONFIG.auto_save_config if target == "config" else API_CONFIG.auto_save_chat
        return f"🔍 {target}自动保存状态: {'✅ 开启' if status else '❌ 关闭'}"

    # 设置状态
    action = parts[1].lower()
    if action not in ("on", "off"):
        return "❌ 无效操作，请输入 on 或 off"

    if target == "config":
        API_CONFIG.auto_save_config = (action == "on")
    else:
        API_CONFIG.auto_save_chat = (action == "on")

    save_config()
    API_CONFIG.last_config_save = True
    return f"✅ {target}自动保存已{'开启' if action == 'on' else '关闭'}"


def handle_summary_command(parts: List[str]) -> str:
    """升级版摘要方案命令"""
    if not parts or parts[0].lower() == "view":
        method_desc = {
            1: "首问提取 - 使用对话第一个问题生成文件名",
            2: "关键词提取 - 分析内容提取高频关键词",
            3: "AI智能摘要 - 使用AI生成精准摘要"
        }
        return (
                f"当前摘要方案: {API_CONFIG.summary_method.name}\n"
                "可用方案:\n" +
                "\n".join([f"{k}. {v}" for k, v in method_desc.items()])
        )

    try:
        choice = int(parts[0])
        method_map = {
            1: SummaryMethod.FIRST_QUESTION,
            2: SummaryMethod.KEYWORDS,
            3: SummaryMethod.AI_SUMMARY
        }
        API_CONFIG.summary_method = method_map[choice]
        save_config()
        return f"✅ 已切换至方案 {choice}: {API_CONFIG.summary_method.name}"
    except (ValueError, KeyError):
        return "❌ 无效方案，请输入1-3的数字"


def handle_save_command(history: List[Dict[str, str]], parts: List[str]) -> str:
    """增强版保存命令"""
    targets = {"config", "chat", "all"}
    if not parts:
        return save_conversation(history, [])  # 默认保存聊天

    target = parts[0].lower()
    if target not in targets:
        return f"❌ 无效目标，可选: {', '.join(targets)}"

    results = []
    if target in ("config", "all"):
        save_config()
        API_CONFIG.last_config_save = True
        results.append("✅ 配置已保存")
    if target in ("chat", "all"):
        chat_args = parts[1:] if target == "all" else parts[2:]
        chat_result = save_conversation(history, chat_args)
        results.append(chat_result)

    return "\n".join(results)


def exit_procedure(history) -> str:
    """智能退出流程"""
    save_actions = []

    # 配置自动保存逻辑
    if API_CONFIG.auto_save_config and not API_CONFIG.last_config_save:
        save_config()
        save_actions.append("✅ 配置已自动保存")

    # 聊天自动保存逻辑
    if API_CONFIG.auto_save_chat and not API_CONFIG.last_chat_save:
        save_result = save_conversation(history, [])
        save_actions.append(save_result)

    # 重置标记
    API_CONFIG.last_config_save = False
    API_CONFIG.last_chat_save = False

    if save_actions:
        return "\n".join(save_actions) + "\n🛑 对话结束"
    return "🛑 对话结束"


# ================= 帮助信息更新 =================
def show_help(cmd: str = "") -> str:
    help_texts = {
        "help": """
        /help [命令名称] - 显示帮助信息
        示例：
        /help        - 显示所有命令
        /help save   - 显示save命令帮助
        """,
        "reset": """
        /reset - 重置对话历史
        将清除当前对话内容，恢复到初始状态""",
        "save": """
        /save [目标] [参数] - 手动保存内容
        目标可选：
        config - 仅保存配置
        chat   - 保存聊天记录（默认）
        all    - 保存配置和聊天
        示例：
        /save chat 我的对话 - 保存聊天记录
        /save all          - 保存配置和聊天""",
        "load": """
        /load [文件名] - 加载历史对话
        参数说明：
        文件名：可选，不填则加载最新记录
        示例：
        /load         - 加载最新对话
        /load 我的对话 - 加载指定文件""",
        "summary": """
        /summary [view|编号] - 管理摘要方案
        编号：
        1. 首问提取  2. 关键词提取  3. AI摘要
        示例：
        /summary      - 查看当前方案
        /summary 2    - 切换至关键词方案""",
        "exit": """
        /exit 或 /quit - 退出程序
        退出前会根据设置自动保存""",
        "autosave": """
        /autosave [config|chat|all] [on|off|view] - 管理自动保存
        示例：
        /autosave config on   - 开启配置自动保存
        /autosave chat view   - 查看聊天保存状态
        /autosave all view    - 查看全部保存状态"""
    }

    border = "=" * 40
    if not cmd:
        return f"{border}\n 可用命令列表（输入/help 命令 以查看具体帮助信息。如/help help） \n{border}\n" + "\n".join(
            f" ▪ /{name}" for name in help_texts.keys())

    if cmd in help_texts:
        return f"{border}\n 命令帮助：/{cmd} \n{border}{help_texts[cmd]}\n{border}"

    return f"{border}\n 未知命令: {cmd} \n{border}"


def reset_conversation(history: List[Dict[str, str]]) -> str:
    try:
        system_msg = next((msg for msg in history if msg["role"] == "system"), None)
        history.clear()
        if system_msg:
            history.append(system_msg)
        else:
            history.append({"role": "system", "content": API_CONFIG.system_message})
        return "✅ 对话历史已重置"
    except Exception as e:
        return f"❌ 重置失败: {str(e)}"


def handle_autosave_command(parts: List[str]) -> str:
    if not parts or parts[0].lower() == "all":
        return (
            "🔄 自动保存状态:\n"
            f"• 配置自动保存: {'✅ 开启' if API_CONFIG.auto_save_config else '❌ 关闭'}\n"
            f"• 聊天自动保存: {'✅ 开启' if API_CONFIG.auto_save_chat else '❌ 关闭'}\n"
            "使用 /autosave [config|chat] [on|off|view] 管理"
        )

    target = parts[0].lower()
    if target not in ("config", "chat"):
        return "❌ 无效目标，请输入 config 或 chat"

    if len(parts) == 1 or (len(parts) > 1 and parts[1].lower() == "view"):
        status = API_CONFIG.auto_save_config if target == "config" else API_CONFIG.auto_save_chat
        return f"🔍 {target}自动保存状态: {'✅ 开启' if status else '❌ 关闭'}"

    action = parts[1].lower()
    if action not in ("on", "off"):
        return "❌ 无效操作，请输入 on 或 off"

    if target == "config":
        API_CONFIG.auto_save_config = (action == "on")
    else:
        API_CONFIG.auto_save_chat = (action == "on")

    save_config()
    API_CONFIG.last_config_save = True
    return f"✅ {target}自动保存已{'开启' if action == 'on' else '关闭'}"


def handle_command(cmd: str, parts: List[str], history: List[Dict[str, str]]) -> Tuple[bool, str]:
    command_handlers = {
        "help": lambda: (False, show_help(parts[1].lower() if len(parts) > 1 else "")),
        "reset": lambda: (False, reset_conversation(history)),
        "save": lambda: (False, handle_save_command(history, parts[1:])),
        "load": lambda: (False, load_procedure(history, parts)),
        "summary": lambda: (False, handle_summary_command(parts[1:])),
        "autosave": lambda: (False, handle_autosave_command(parts[1:])),
        "exit": lambda: (True, exit_procedure(history)),
        "quit": lambda: (True, exit_procedure(history))
    }

    handler = command_handlers.get(cmd.lower())
    return handler() if handler else (False, f"❌ 未知命令: {cmd}\n{show_help()}")


def load_procedure(history, parts):
    if len(parts) > 2:
        return "❌ 错误：只能指定一个文件名"
    loaded_history, message = load_conversation(parts[1:])
    if loaded_history:
        history[:] = loaded_history
        return f"{message}\n📝 最后对话内容：{history[-1]['content'][:50]}..."
    return message


def exit_procedure(history) -> str:
    save_actions = []

    if API_CONFIG.auto_save_config and not API_CONFIG.last_config_save:
        save_config()
        save_actions.append("✅ 配置已自动保存")

    if API_CONFIG.auto_save_chat and not API_CONFIG.last_chat_save:
        save_result = save_conversation(history, [])
        save_actions.append(save_result)

    API_CONFIG.last_config_save = False
    API_CONFIG.last_chat_save = False

    if save_actions:
        return "\n".join(save_actions) + "\n🛑 对话结束"
    return "🛑 对话结束"


def main():
    load_config()
    client = openai.OpenAI(
        api_key=API_CONFIG.api_key,
        base_url=API_CONFIG.base_url,
        timeout=API_CONFIG.timeout
    )

    conversation_history = [
        {"role": "system", "content": API_CONFIG.system_message}
    ]

    if latest := get_latest_file():
        choice = input(f"📂 检测到最新对话记录 {os.path.basename(latest)}，是否加载？(y/n): ").lower()
        if choice == 'y':
            loaded, msg = load_conversation([])
            if loaded:
                conversation_history = loaded
                print(f"{msg}\n💬 最后对话内容：{conversation_history[-1]['content'][:50]}...")

    printer = StreamPrinter()

    while True:
        try:
            user_input = input("\n👤 您：").strip()
            if not user_input:
                continue

            if user_input.lower() in ('exit', 'quit'):
                user_input = '/' + user_input

            if user_input.startswith('/'):
                parts = user_input[1:].split()
                cmd = parts[0].lower() if parts else ""
                exit_flag, message = handle_command(cmd, parts, conversation_history)
                print(message)
                if exit_flag:
                    break
                continue

            if len(user_input) > 2000:
                print("⚠️ 输入超过2000字符，请精简内容")
                continue

            conversation_history.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(
                model=API_CONFIG.model,
                messages=trim_history(conversation_history, API_CONFIG.max_history),
                stream=True,
                max_tokens=3000,
                temperature=1.3,
                presence_penalty=0.5
            )

            assistant_response = printer.print_stream(response)

            if assistant_response:
                conversation_history.append(
                    {"role": "assistant", "content": assistant_response}
                )

        except openai.APITimeoutError:
            print("\n⏳ 请求超时，请检查网络连接")
            if conversation_history[-1]["role"] == "user":
                conversation_history.pop()
        except Exception as e:
            print(f"\n❌ 发生错误: {str(e)}")
            if conversation_history and conversation_history[-1]["role"] == "user":
                conversation_history.pop()


if __name__ == "__main__":
    print("🌟 欢迎使用智能助手JunhaxAI！本系统集成先进AI模型，为您提供专业智能服务。")
    print("📝 输入 /help 获取帮助信息")
    print("©️ Junhax AI 工作室，保留所有权利\n" + "=" * 50)
    main()
