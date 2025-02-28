import json
import os
import tempfile
from colorama import init, Fore, Style
from openai import OpenAI

# 缓存文件配置
CACHE_FILE = os.path.join(tempfile.gettempdir(), "chat_cache.json")
print(tempfile.gettempdir())

first_run = True

init()

def load_cache():
    """加载对话历史缓存"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"\n⚠️ 缓存加载失败: {str(e)}，将创建新对话")
    return [{"role": "system", "content": "你是一个助手，需要用中文回答"}]


def save_cache(messages):
    """保存对话历史到硬盘"""
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"\n⚠️ 缓存保存失败: {str(e)}")


client = OpenAI(
    api_key="sk-Qo8c77pIOMToiZ8y8fD92b7d096c471896B064C14c8809A9",
    base_url="https://maas-api.cn-huabei-1.xf-yun.com/v1",
    max_retries=5
)

# 初始化对话历史（带缓存加载）
messages = load_cache()


def process_stream_response(response):
    """处理流式响应并返回完整回答"""
    reasoning_content = ""
    content = ""
    reasoning_times = 1
    content_times = 1

    for chunk in response:
        if hasattr(chunk.choices[0].delta, "reasoning_content") and chunk.choices[0].delta.reasoning_content:
            if reasoning_times == 1:
                print(Fore.LIGHTBLACK_EX+"\n⚡️推理内容：", end=""+Style.RESET_ALL)
            reasoning_content += chunk.choices[0].delta.reasoning_content
            print(Fore.LIGHTBLACK_EX+chunk.choices[0].delta.reasoning_content, end=""+Style.RESET_ALL)
            reasoning_times += 1
        else:
            current_content = str(getattr(chunk.choices[0].delta, "content", ""))
            current_content = current_content.replace('\n', '')
            if current_content:
                if content_times == 1:
                    print("\n💬AI回答：", end="")
                content += current_content
                print(current_content, end="", flush=True)
                content_times += 1

    return content


# 多轮对话循环
while True:
    if (first_run):
        user_input = input("👤您：")
        first_run = False
    else:
        user_input=input("\n\n👤您：")
    if user_input.lower() in ["/exit"]:
        print("\n🔚对话结束")
        # 退出时清除缓存
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)
        break

    messages.append({"role": "user", "content": user_input})
    save_cache(messages)  # 立即保存用户输入

    response = client.chat.completions.create(
        model="xdeepseekr1",
        messages=messages,
        stream=True
    )

    assistant_response = process_stream_response(response)

    if assistant_response:
        messages.append({"role": "assistant", "content": assistant_response})
        save_cache(messages)  # 保存完整对话