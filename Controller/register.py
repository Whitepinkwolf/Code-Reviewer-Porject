import re

from PyQt5.QtWidgets import *
from UI.registerWidget import Ui_Register
from Data import leanCloud
from leanCloud import *
from PyQt5.QtCore import pyqtSignal,Qt


class MainRegistWindow(QWidget, Ui_Register):
    SuccessReg = pyqtSignal()  # 定义一个注册成功信号
    ReturnLogin = pyqtSignal()  # 定义一个返回登录界面的信号

    def __init__(self, parent=None):
        super(MainRegistWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.UserNameReEdit.setFocus()  # 鼠标焦点
        self.UserNameReEdit.setPlaceholderText("请输入注册用户名")
        self.PasswordReEdit.setPlaceholderText("请输入密码")
        self.ComfirmPwEdit.setPlaceholderText("请确认密码")
        self.PasswordReEdit.setEchoMode(QLineEdit.Password)  # 密码隐藏
        self.ComfirmPwEdit.setEchoMode(QLineEdit.Password)

        # self.UserNameReEdit.textChanged.connect(self.emit_Username)  # 用户名
        # self.PasswordReEdit.textChanged.connect(self.emit_Password)  # 密码
        # self.ComfirmPwEdit.textChanged.connect(self.emit_ConPassword)  # 确认密码
        self.ComFirmReButton.clicked.connect(self.emit_Confir_Button)  # 确认按钮
        self.ReturnReButton.clicked.connect(self.emit_Cancel)  # 返回按钮

    # def emit_Username(self):
    #     print("UserName发生改变")
    #
    # def emit_Password(self):
    #     print("PassWord发生改变")
    #
    # def emit_ConPassword(self):
    #     print("ConPassword发生改变")

    def emit_Confir_Button(self):

        if self.UserNameReEdit.text().strip() == '':
            QMessageBox.information(self, "error", "请输入用户名!")
        elif self.PasswordReEdit.text().strip() == '':
            QMessageBox.information(self, "error", "请输入密码!")
        elif self.ComfirmPwEdit.text().strip() == '':
            QMessageBox.information(self, "error", "请输入确认密码!")

        elif self.UserNameReEdit.text().strip() != ''\
                and self.PasswordReEdit.text().strip() != '' \
                and self.ComfirmPwEdit.text().strip() != '':

            if len(self.PasswordReEdit.text()) < 6 or len(self.PasswordReEdit.text()) > 18:
                QMessageBox.information(self, "warning", "密码应在6-18位之间！")
            elif not re.search(r'\d', self.ComfirmPwEdit.text()) or not re.search(r'[a-zA-Z]', self.ComfirmPwEdit.text()):
                QMessageBox.information(self, "Warning", "密码应同时包含字母和数字！")
            elif self.PasswordReEdit.text() != self.ComfirmPwEdit.text():
                QMessageBox.information(self, "error", "两次密码输入不一致！")
            else:
                Re_UserName = self.UserNameReEdit.text()
                Re_PassWord = self.PasswordReEdit.text()

                query_Passwd = UserQuery(Re_UserName)
                if query_Passwd == None:
                    UserStore(Re_UserName, Re_PassWord)
                    QMessageBox.information(self, "successful", "注册成功!")
                    self.SuccessReg.emit()
                else:
                    QMessageBox.information(self, "error", "该用户名已存在！")

    def emit_Cancel(self):
        self.ReturnLogin.emit()