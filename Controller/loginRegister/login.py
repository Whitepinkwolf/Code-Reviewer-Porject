from PyQt5.QtWidgets import *

from Data.leanCloud import UserQuery
from UI.loginRegister.loginWidget import Ui_Login
from register import MainRegistWindow

from Controller.menu import Menu

import sys
import configparser
import os

global UserName
UserP = {}  # 定义一个存储密码账号的元组

filePath = os.path.dirname(os.getcwd())+"\\Data\\user.ini"


class MainLoginWindow(QWidget, Ui_Login):
    def __init__(self, parent=None):
        super(MainLoginWindow, self).__init__(parent)
        self.re = MainRegistWindow()  # 这边一定要加self
        self.mainWin = Menu()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.IsRememberUser()
        self.UserNameEdit.setFocus()
        self.UserNameEdit.setPlaceholderText("请输入账号")
        self.PassWordEdit.setPlaceholderText("请输入密码")
        self.PassWordEdit.setEchoMode(QLineEdit.Password)  # 密码隐藏

        self.RegisterButton.clicked.connect(self.regist_button)  # 跳转到注册页面
        self.re.SuccessReg.connect(self.Success_Regist)  # 注册成功跳转回来
        self.re.ReturnLogin.connect(self.Return_Login)  # 返回 跳转回来
        self.LoginButton.clicked.connect(self.login_button)  # 登录

    """设置记住密码"""
    def IsRememberUser(self):
        config = configparser.ConfigParser()
        file = config.read(filePath)  # 读取密码账户的配置文件
        config_dict = config.defaults()  # 返回包含实例范围默认值的字典
        self.account = config_dict['user_name']  # 获取账号信息
        self.UserNameEdit.setText(self.account)  # 写入账号上面
        if config_dict['remember'] == 'True':
            self.passwd = config_dict['password']
            self.PassWordEdit.setText(self.passwd)
            self.RememberPwcheckBox.setChecked(True)
        else:
            self.RememberPwcheckBox.setChecked(False)

    """设置配置文件格式"""
    def config_ini(self):
        self.account = self.UserNameEdit.text()
        self.passwd = self.PassWordEdit.text()
        config = configparser.ConfigParser()
        if self.RememberPwcheckBox.isChecked():
            config["DEFAULT"] = {
                "user_name": self.account,
                "password": self.passwd,
                "remember": self.RememberPwcheckBox.isChecked()
            }
        else:
            config["DEFAULT"] = {
                "user_name": self.account,
                "password": "",
                "remember": self.RememberPwcheckBox.isChecked()
            }
        with open(filePath, 'w') as configfile:
            config.write(configfile)
        print(self.account, self.passwd)

    # 注册
    def regist_button(self):
        # 载入数据库
        # self.sql = Oper_Mysql()
        # self.sql.ZSGC_Mysql()
        self.re.show()
        LoginWin.close()

    # 登录
    def login_button(self):

        Login_UserName = self.UserNameEdit.text()
        Login_Passwd = self.PassWordEdit.text()

        if Login_UserName.strip() == '' or Login_Passwd.strip() == '':
            QMessageBox.information(self, "error", "请输入用户名和密码！")
        else:
            self.config_ini()  # 加载用户密码配置文件
            query_Passwd = UserQuery(Login_UserName)
            if query_Passwd == None:
                QMessageBox.information(self, "waining", "该账号不存在！", QMessageBox.Ok)
                return False
            else:
                if query_Passwd == Login_Passwd:  # 登陆成功
                    mess = QMessageBox()
                    mess.setWindowTitle("Success")
                    mess.setText("登录成功！")
                    mess.setStandardButtons(QMessageBox.Ok)
                    mess.button(QMessageBox.Ok).animateClick(1000)  # 弹框定时关闭
                    mess.exec_()
                    print("登录成功")
                    self.mainWin.show()
                    LoginWin.close()  # 关闭 LoginWin
                    return True
                else:
                    QMessageBox.information(self, "error!", "密码错误！", QMessageBox.Ok)
                    return False

    # 成功注册
    def Success_Regist(self):
        LoginWin.show()
        self.re.close()

    # 返回
    def Return_Login(self):
        LoginWin.show()
        self.re.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    LoginWin = MainLoginWindow()
    LoginWin.show()
    sys.exit(app.exec())

