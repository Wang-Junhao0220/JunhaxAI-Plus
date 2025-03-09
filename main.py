import os
import sys

from core import RequestResponse, PrintContents
from PyQt5 import QtWidgets, QtCore

from ui.logic_settingsWindow import LogicSettingsWindow
from ui.logic_mainWindow import LogicMainWindow

def test_multi_turn_conversation():
    # 第一次对话
    first_message = input("You:")
    first_response = RequestResponse.request_response(first_message, "xdeepseekr1", stream_response=True)
    print("🐳 DeepSeek:")
    PrintContents.print_response(first_response, True, True)
def launch_settings_window():
    # while True:
    #     test_multi_turn_conversation()
    os.environ['QT_ENABLE_HIGHDPI_SCALING'] = '1'
    through = QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(through)

    app = QtWidgets.QApplication(sys.argv)
    app_settings_window = LogicMainWindow()
    app_settings_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_settings_window()
