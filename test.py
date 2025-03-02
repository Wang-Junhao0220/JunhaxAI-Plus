from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QFormLayout, QLabel, QLineEdit, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tabWidget = QTabWidget(self)

        # General Tab
        general_tab = QWidget()
        form_layout_general = QFormLayout(general_tab)
        form_layout_general.addRow(QLabel("Name:"), QLineEdit())
        form_layout_general.addRow(QLabel("Email:"), QLineEdit())
        self.tabWidget.addTab(general_tab, "General")

        # Tab 2
        tab2 = QWidget()
        form_layout_tab2 = QFormLayout(tab2)
        form_layout_tab2.addRow(QLabel("Address:"), QLineEdit())
        form_layout_tab2.addRow(QLabel("Phone:"), QLineEdit())
        self.tabWidget.addTab(tab2, "Tab 2")

        # 设置默认选中General
        self.tabWidget.setCurrentIndex(0)

        # 窗口布局
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.tabWidget)
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()