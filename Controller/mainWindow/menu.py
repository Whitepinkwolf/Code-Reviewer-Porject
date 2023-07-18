import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from Controller.extentDetect.extentWidget import extent_Widget
from Controller.codeAudit.codeAuditWidget import codeAudit_Widget
from Controller.riskFunction.manageRiskFunctionWidget import manageRiskFunction_Widget

from UI.menu import Ui_menu
from Tool.Animation import UIFunction

class Menu(QWidget, Ui_menu):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.uifunction = UIFunction(self)

        self.loginWin = None

        # 透明化
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)

        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.HidePushButton.clicked.connect(self.menu_hide)

        # 连接按钮的点击事件到对应的槽函数
        self.Page1pushButton.clicked.connect(self.show_widget_1)
        self.Page2pushButton.clicked.connect(self.show_widget_2)
        self.Page3pushButton.clicked.connect(self.show_widget_3)
        self.ExitPushButton.clicked.connect(self.close_Event)

    def menu_hide(self):
        if self.HidePushButton.text() == "<":
            self.HidePushButton.setText(">")
        elif self.HidePushButton.text() == ">":
            self.HidePushButton.setText("<")
        self.uifunction.MeauFunction()
        pass

    def show_widget_1(self):
        widget = codeAudit_Widget()
        self.ChangeStackedWidget.addWidget(widget)
        self.ChangeStackedWidget.setCurrentWidget(widget)

    def show_widget_2(self):
        widget = manageRiskFunction_Widget()
        self.ChangeStackedWidget.addWidget(widget)
        self.ChangeStackedWidget.setCurrentWidget(widget)

    def show_widget_3(self):
        widget = extent_Widget()
        self.ChangeStackedWidget.addWidget(widget)
        self.ChangeStackedWidget.setCurrentWidget(widget)

    def close_Event(self):
        self.box = QMessageBox(QMessageBox.Question, '退出', '确定要退出吗？')
        yes1 = self.box.addButton('退出登陆', QMessageBox.YesRole)
        yes2 = self.box.addButton('退出', QMessageBox.NoRole)
        # 显示该问答框作为模态对话框
        result = self.box.exec_()
        if self.box.clickedButton() == yes1:
            print(11)
            from Controller.loginRegister.login import MainLoginWindow
            # 创建或获取LoginWin窗口实例

            if self.loginWin is None:
                self.loginWin = MainLoginWindow()
            self.loginWin.show()
            win.close()  # 关闭 Menu
            print(11)
        elif self.box.clickedButton() == yes2:
            QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Menu()
    win.show()
    sys.exit(app.exec_())
