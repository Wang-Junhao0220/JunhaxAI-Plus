from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ui_settingsWindow import Ui_SettingsWindow
import os
import sys


class LogicSettingsWindow(QtWidgets.QMainWindow):
    def __init__ (self, parent=None):
        super().__init__(parent)
        self.ui=Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.ui.settingsWidget.setCurrentIndex(0)