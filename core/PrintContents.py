from colorama import init, Fore, Style
from HistoryChatManager import HistoryChatManager

# 初始化历史记录管理器
history_manager = HistoryChatManager()
# 初始化colorama
init()

def print_reasoning_content(content,reasoning_time=1):
    if reasoning_time==1:
        print(Style.BRIGHT + Fore.LIGHTBLACK_EX + "⚡️ Reasoning Content: " + Style.RESET_ALL)
    """打印推理内容，灰色加粗"""
    if content:
        print(Fore.LIGHTBLACK_EX + content + Style.RESET_ALL)

def print_ai_response(content,content_time=1):
    if content_time==1:
        print(Style.BRIGHT +Fore.BLACK+ "💬 AI Response: " + Style.RESET_ALL)
    """打印AI回答，加粗"""
    if content:
        print(content)

def process_stream_response(response, include_reasoning):
    """处理流式响应并返回完整回答"""
    reasoning_content = ""
    content = ""
    reasoning_times = 1
    content_times = 1

    for chunk in response:
        if include_reasoning and chunk.choices[0].delta.reasoning_content:
            if reasoning_times == 1:
                print_reasoning_content("")
            reasoning_content += chunk.choices[0].delta.reasoning_content
            print(Fore.LIGHTBLACK_EX + chunk.choices[0].delta.reasoning_content, end="", flush=True)
            reasoning_times += 1
        else:
            current_content = str(getattr(chunk.choices[0].delta, "content", ""))
            current_content = current_content.replace('\n', '')
            if current_content:
                if content_times == 1:
                    print_ai_response("")
                content += current_content
                print(current_content, end="", flush=True)
                content_times += 1

    print()  # 确保换行
    return content, reasoning_content

def process_non_stream_response(response, include_reasoning):
    """处理非流式响应"""
    if include_reasoning:
        print_reasoning_content(response.choices[0].message.reasoning_content)
        print_ai_response(response.choices[0].message.content)
        return response.choices[0].message.content, response.choices[0].message.reasoning_content
    else:
        print_ai_response(response.choices[0].message.content)
        return response.choices[0].message.content, None

def print_response(response, is_stream, include_reasoning=False):
    """打印响应内容，支持流式和非流式"""
    if is_stream:
        response_text, reasoning_content = process_stream_response(response, include_reasoning)
    else:
        response_text, reasoning_content = process_non_stream_response(response, include_reasoning)
    
    # 将AI的回答添加到历史记录中
    if response_text:
        history_manager.add_message("assistant", response_text)