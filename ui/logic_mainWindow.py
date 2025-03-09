import qdarkstyle
from PyQt5 import QtWidgets

from ui.ui_settingsWindow import Ui_SettingsWindow
from ui.ui_mainwindow import Ui_MainWindow
from ui.logic_settingsWindow import LogicSettingsWindow
from styleSheets import styleSheets


class LogicMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LogicMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionPreferences.triggered.connect(self.launch_settings_window)

    def launch_settings_window(self):
        settings_window = LogicSettingsWindow()
        settings_window.show()
        settings_window.exec_()
