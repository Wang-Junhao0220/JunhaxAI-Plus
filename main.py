# # 导入
# from core import PrintContents, RequestResponse
#
#
# # TODO: 修复启用推理AI Response后面的两个换行 ✔
#
#
# # Bug: 流式响应无法打印 2025-02-22-22：55：30
# # 测试多轮对话功能


# imports
import os
# 创建SettingsWindow窗体
import qdarkstyle
import sys

from core import RequestResponse, PrintContents
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from ui.logic_settingsWindow import LogicSettingsWindow

def test_multi_turn_conversation():
    # 第一次对话
    first_message = input("You:")
    first_response = RequestResponse.request_response(first_message, "xdeepseekr1", stream_response=True)
    print("🐳 DeepSeek:")
    PrintContents.print_response(first_response, True, True)
    # 第二次对话，传递历史消息
    #second_message = "What did I say? tell me"
    #second_response = RequestResponse.request_response(second_message, "xdeepseekr1", stream_response=True)
    #PrintContents.print_response(second_response, True, True)
# 运行测试
# test_multi_turn_conversation()

def launch_settings_window():
    while True:
        test_multi_turn_conversation()
    os.environ['QT_ENABLE_HIGHDPI_SCALING'] = '1'
    through = QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(through)
    app = QtWidgets.QApplication(sys.argv)
    app_settings_window = LogicSettingsWindow()

    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    app_settings_window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    launch_settings_window()
