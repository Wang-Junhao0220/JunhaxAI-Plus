# 导入core
import PrintContents
import RequestResponse

# TODO: 修复启用推理AI Response后面的两个换行 ✔


# Bug: 流式响应无法打印 2025-02-22-22：55：30
# 测试多轮对话功能
def test_multi_turn_conversation():
    # 第一次对话
    first_message = "Hello! How are you?"
    first_response = RequestResponse.request_response(first_message, "xdeepseekr1", stream_response=True)
    PrintContents.print_response(first_response, True,True)

    # 第二次对话，传递历史消息
    second_message = "What did I say? tell me"
    second_response = RequestResponse.request_response(second_message, "xdeepseekr1", stream_response=True)
    PrintContents.print_response(second_response, True,True)


# 运行测试
test_multi_turn_conversation()
