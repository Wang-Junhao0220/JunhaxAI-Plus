# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
from PrintContents import history_manager  # 引入history_manager

# API_KEY = "sk-412f81f433a74a8dbce46756d9acd508"
# BASE_URL = "https://api.deepseek.com"
SYSTEM_MESSAGE = "You are a helpful assistant, answers should be as simple as possible and reasoning should be as simple as possible"
TEMPERATURE = 0.8
MAX_TOKENS = 4096
MODEL_NAME = "xdeepseekv3"
API_KEY = "sk-Qo8c77pIOMToiZ8y8fD92b7d096c471896B064C14c8809A9"
BASE_URL = "https://maas-api.cn-huabei-1.xf-yun.com/v1"


def create_client(api_key=API_KEY, base_url=BASE_URL):
    client = OpenAI(api_key=api_key, base_url=base_url)
    return client


def change_system_message(new_sys_message):
    global SYSTEM_MESSAGE
    SYSTEM_MESSAGE = new_sys_message


def change_temperature(new_temperature):
    # 增加验证器，保证 temperature在0-1之间
    if new_temperature < 0 or new_temperature > 1:
        raise ValueError("temperature must be between 0 and 1")
    global TEMPERATURE
    TEMPERATURE = new_temperature


def change_max_tokens(new_max_tokens):
    global MAX_TOKENS
    MAX_TOKENS = new_max_tokens


def change_model_name(new_model_name):
    global MODEL_NAME
    MODEL_NAME = new_model_name


def request_response(user_message, model_name=MODEL_NAME, previous_messages=None, stream_response=True,
                     system_messgae=SYSTEM_MESSAGE, temperature=TEMPERATURE, max_tokens=MAX_TOKENS):
    messages = [{"role": "system", "content": system_messgae}]
    
    # 如果存在之前的消息，将其合并
    if previous_messages:
        messages.extend(previous_messages)
    else:
        # 自动获取历史消息
        messages.extend(history_manager.get_history())
    
    # 添加用户消息
    messages.append({"role": "user", "content": user_message})
    history_manager.add_message("user", user_message)

    # print(messages)

    response = create_client().chat.completions.create(
        model=model_name,
        messages=messages,
        stream=stream_response,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response