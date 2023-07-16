# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(1475, 886)
        self.HidePushButton = QtWidgets.QPushButton(menu)
        self.HidePushButton.setGeometry(QtCore.QRect(110, 150, 41, 41))
        self.HidePushButton.setObjectName("HidePushButton")
        self.widget = QtWidgets.QWidget(menu)
        self.widget.setGeometry(QtCore.QRect(0, 0, 131, 941))
        self.widget.setObjectName("widget")
        self.ExitPushButton = QtWidgets.QPushButton(self.widget)
        self.ExitPushButton.setGeometry(QtCore.QRect(0, 550, 131, 61))
        self.ExitPushButton.setObjectName("ExitPushButton")
        self.Page3pushButton = QtWidgets.QPushButton(self.widget)
        self.Page3pushButton.setGeometry(QtCore.QRect(0, 440, 131, 61))
        self.Page3pushButton.setObjectName("Page3pushButton")
        self.Page2pushButton = QtWidgets.QPushButton(self.widget)
        self.Page2pushButton.setGeometry(QtCore.QRect(0, 330, 131, 61))
        self.Page2pushButton.setObjectName("Page2pushButton")
        self.Page1pushButton = QtWidgets.QPushButton(self.widget)
        self.Page1pushButton.setGeometry(QtCore.QRect(0, 220, 131, 61))
        self.Page1pushButton.setObjectName("Page1pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.ChangeStackedWidget = QtWidgets.QStackedWidget(menu)
        self.ChangeStackedWidget.setGeometry(QtCore.QRect(159, 9, 1321, 871))
        self.ChangeStackedWidget.setObjectName("ChangeStackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.ChangeStackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.ChangeStackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.ChangeStackedWidget.addWidget(self.page3)

        self.retranslateUi(menu)
        self.ChangeStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Form"))
        self.HidePushButton.setText(_translate("menu", "<"))
        self.ExitPushButton.setText(_translate("menu", "退出"))
        self.Page3pushButton.setText(_translate("menu", "扩展应用"))
        self.Page2pushButton.setText(_translate("menu", "审计管理"))
        self.Page1pushButton.setText(_translate("menu", "代码审计"))

