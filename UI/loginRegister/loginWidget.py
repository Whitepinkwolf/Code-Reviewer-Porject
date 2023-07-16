# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1038, 521)
        self.LoginButton = QtWidgets.QPushButton(Login)
        self.LoginButton.setGeometry(QtCore.QRect(692, 337, 281, 41))
        self.LoginButton.setObjectName("LoginButton")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(771, 54, 141, 41))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(690, 140, 311, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.UserNameEdit = QtWidgets.QLineEdit(self.frame)
        self.UserNameEdit.setGeometry(QtCore.QRect(90, 10, 191, 31))
        self.UserNameEdit.setObjectName("UserNameEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 0, 51, 51))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 10, 31, 31))
        self.graphicsView.setObjectName("graphicsView")
        self.frame_2 = QtWidgets.QFrame(Login)
        self.frame_2.setGeometry(QtCore.QRect(690, 220, 311, 31))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.PassWordEdit = QtWidgets.QLineEdit(self.frame_2)
        self.PassWordEdit.setGeometry(QtCore.QRect(90, 0, 191, 31))
        self.PassWordEdit.setObjectName("PassWordEdit")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 0, 51, 31))
        self.label_3.setObjectName("label_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.RegisterButton = QtWidgets.QPushButton(Login)
        self.RegisterButton.setGeometry(QtCore.QRect(690, 400, 281, 41))
        self.RegisterButton.setObjectName("RegisterButton")
        self.RememberPwcheckBox = QtWidgets.QCheckBox(Login)
        self.RememberPwcheckBox.setGeometry(QtCore.QRect(690, 280, 91, 31))
        self.RememberPwcheckBox.setObjectName("RememberPwcheckBox")
        self.ForgetPwButton = QtWidgets.QPushButton(Login)
        self.ForgetPwButton.setGeometry(QtCore.QRect(880, 280, 93, 31))
        self.ForgetPwButton.setObjectName("ForgetPwButton")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Login)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 0, 631, 521))
        self.graphicsView_3.setObjectName("graphicsView_3")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.LoginButton.setText(_translate("Login", "登陆"))
        self.label.setText(_translate("Login", "    xxxx系统"))
        self.label_2.setText(_translate("Login", "用户名"))
        self.label_3.setText(_translate("Login", " 密码"))
        self.RegisterButton.setText(_translate("Login", "注册"))
        self.RememberPwcheckBox.setText(_translate("Login", "记住密码"))
        self.ForgetPwButton.setText(_translate("Login", "找回密码"))

