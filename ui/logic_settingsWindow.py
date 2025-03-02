import qdarkstyle
from PyQt5 import QtWidgets

from ui.ui_settingsWindow import Ui_SettingsWindow
from styleSheets import styleSheets


class LogicSettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.ui.settingsWidget.setCurrentIndex(0)
        # load_default_settings函数写好之后改掉
        self.ui.streamChoice.setCurrentIndex(0)  # 0->Enabled
        self.ui.recoverChatChoice.setCurrentIndex(0)  # 0->Enabled
        self.ui.autoSaveChatChoice.setCurrentIndex(0)  # 0->Immediately
        self.ui.multiTurnChoice.setCurrentIndex(0)  # 0->Enabled
        self.ui.maxResponseEdit.setText("4096")  # Default max response tokens

        self.monitor()


    # 绑定槽函数之函数
    def monitor(self):
        self.ui.themeChoice.currentIndexChanged.connect(self.change_theme)
        self.ui.historyManBtn.clicked.connect(self.test_connect)

    def load_default_settings(self):
        pass

    def change_theme(self):
        print("RECEIVE SIGNAL")
        getQss=styleSheets.styleSheets()
        new_theme = self.ui.themeChoice.currentText()
        if new_theme == "System":
            self.setStyleSheet("") # 清除样式
        elif new_theme == "Darcula":
            # set darcula style
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        elif new_theme == "ElegantDark":
            self.setStyleSheet(getQss.get_style(getQss,"ElegantDark"))
        elif new_theme == "ManjaroMix":
            self.setStyleSheet(getQss.get_style(getQss,"ManjaroMix"))
        elif new_theme == "MaterialDark":
            self.setStyleSheet(getQss.get_style(getQss,"MaterialDark"))
        elif new_theme == "Ubuntu":
            self.setStyleSheet(getQss.get_style(getQss,"Ubuntu"))
        elif new_theme == "aqua":
            self.setStyleSheet(getQss.get_style(getQss,"aqua"))
        elif new_theme == "AMOLED":
            self.setStyleSheet(getQss.get_style(getQss,"AMOLED"))
        elif new_theme=="ConsoleStyle":
            self.setStyleSheet(getQss.get_style(getQss,"ConsoleStyle"))

    def test_connect(self):
        print("CONNECTED!")



# Hi! Here is a problem about slot binding
# Look Upon.