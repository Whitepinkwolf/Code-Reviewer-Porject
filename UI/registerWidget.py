# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(557, 368)
        self.label = QtWidgets.QLabel(Register)
        self.label.setGeometry(QtCore.QRect(230, 50, 72, 31))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Register)
        self.frame.setGeometry(QtCore.QRect(110, 110, 311, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.UserNameReEdit = QtWidgets.QLineEdit(self.frame)
        self.UserNameReEdit.setGeometry(QtCore.QRect(90, 0, 191, 31))
        self.UserNameReEdit.setObjectName("UserNameReEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 71, 31))
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(Register)
        self.frame_2.setGeometry(QtCore.QRect(110, 170, 311, 31))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.PasswordReEdit = QtWidgets.QLineEdit(self.frame_2)
        self.PasswordReEdit.setGeometry(QtCore.QRect(90, 0, 191, 31))
        self.PasswordReEdit.setObjectName("PasswordReEdit")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 71, 31))
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(Register)
        self.frame_3.setGeometry(QtCore.QRect(110, 230, 311, 31))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.ComfirmPwEdit = QtWidgets.QLineEdit(self.frame_3)
        self.ComfirmPwEdit.setGeometry(QtCore.QRect(90, 0, 191, 31))
        self.ComfirmPwEdit.setObjectName("ComfirmPwEdit")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 71, 31))
        self.label_4.setObjectName("label_4")
        self.ComFirmReButton = QtWidgets.QPushButton(Register)
        self.ComFirmReButton.setGeometry(QtCore.QRect(150, 300, 93, 28))
        self.ComFirmReButton.setObjectName("ComFirmReButton")
        self.ReturnReButton = QtWidgets.QPushButton(Register)
        self.ReturnReButton.setGeometry(QtCore.QRect(290, 300, 93, 28))
        self.ReturnReButton.setObjectName("ReturnReButton")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Form"))
        self.label.setText(_translate("Register", "欢迎注册！"))
        self.label_2.setText(_translate("Register", "用户名"))
        self.label_3.setText(_translate("Register", "密码"))
        self.label_4.setText(_translate("Register", "确认密码"))
        self.ComFirmReButton.setText(_translate("Register", "确认"))
        self.ReturnReButton.setText(_translate("Register", "返回"))

