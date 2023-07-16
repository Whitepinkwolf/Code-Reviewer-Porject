import sys

from PyQt5.QtWidgets import QApplication, QWidget

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

    def menu_hide(self):
        # if self.ui.widget.isHidden():
        #     self.ui.widget.show()  # 显示菜单栏
        #     self.ui.widget.setVisible(True)
        #
        # else:
        #     self.ui.widget.hide()  # 隐藏菜单栏
        #     self.ui.widget.setVisible(False)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Menu()
    win.show()
    sys.exit(app.exec_())
