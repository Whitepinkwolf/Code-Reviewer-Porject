# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extentWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_extent(object):
    def setupUi(self, extent):
        extent.setObjectName("extent")
        extent.resize(1546, 860)
        self.commentTabWidget = QtWidgets.QTabWidget(extent)
        self.commentTabWidget.setGeometry(QtCore.QRect(330, 20, 1131, 821))
        self.commentTabWidget.setTabsClosable(True)
        self.commentTabWidget.setMovable(True)
        self.commentTabWidget.setObjectName("commentTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAcceptDrops(False)
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(380, 230, 211, 81))
        self.label_2.setObjectName("label_2")
        self.OpenPushButton = QtWidgets.QPushButton(self.tab)
        self.OpenPushButton.setGeometry(QtCore.QRect(400, 330, 93, 28))
        self.OpenPushButton.setObjectName("OpenPushButton")
        self.commentTabWidget.addTab(self.tab, "")
        self.ChooseActionPushButton = codeAuditMenuButton(extent)
        self.ChooseActionPushButton.setGeometry(QtCore.QRect(60, 30, 181, 41))
        self.ChooseActionPushButton.setObjectName("ChooseActionPushButton")
        self.scrollArea = QtWidgets.QScrollArea(extent)
        self.scrollArea.setGeometry(QtCore.QRect(20, 90, 281, 751))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 749))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeView = QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.treeView.setGeometry(QtCore.QRect(0, 40, 281, 781))
        self.treeView.setObjectName("treeView")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 16))
        self.label.setObjectName("label")
        self.ChooseComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ChooseComboBox.setGeometry(QtCore.QRect(130, 10, 111, 22))
        self.ChooseComboBox.setObjectName("ChooseComboBox")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(extent)
        self.commentTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(extent)

    def retranslateUi(self, extent):
        _translate = QtCore.QCoreApplication.translate
        extent.setWindowTitle(_translate("extent", "Form"))
        self.label_2.setText(_translate("extent", "马上开始使用扩展程序！"))
        self.OpenPushButton.setText(_translate("extent", "打开文件夹"))
        self.commentTabWidget.setTabText(self.commentTabWidget.indexOf(self.tab), _translate("extent", "开始"))
        self.ChooseActionPushButton.setText(_translate("extent", "选择"))
        self.label.setText(_translate("extent", "文件目录"))
        self.ChooseComboBox.setItemText(0, _translate("extent", "*"))
        self.ChooseComboBox.setItemText(1, _translate("extent", "*.c"))
        self.ChooseComboBox.setItemText(2, _translate("extent", "*.h"))
        self.ChooseComboBox.setItemText(3, _translate("extent", "*.c,*.h"))

from codeAuditMenuButton import codeAuditMenuButton
