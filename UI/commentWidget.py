# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commentWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_comment(object):
    def setupUi(self, comment):
        comment.setObjectName("comment")
        comment.resize(971, 807)
        self.scrollArea = QtWidgets.QScrollArea(comment)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 511, 761))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 759))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.commentCodeEditor = NewCodeEditor(self.scrollAreaWidgetContents)
        self.commentCodeEditor.setGeometry(QtCore.QRect(0, 0, 511, 761))
        self.commentCodeEditor.setObjectName("commentCodeEditor")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget = QtWidgets.QStackedWidget(comment)
        self.stackedWidget.setGeometry(QtCore.QRect(530, 40, 441, 751))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 20, 401, 641))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 399, 639))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.ShowDefineTableView = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.ShowDefineTableView.setGeometry(QtCore.QRect(0, 0, 401, 641))
        self.ShowDefineTableView.setObjectName("ShowDefineTableView")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.ShowTextEdit = QtWidgets.QPlainTextEdit(self.page)
        self.ShowTextEdit.setGeometry(QtCore.QRect(10, 680, 401, 61))
        self.ShowTextEdit.setObjectName("ShowTextEdit")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 20, 401, 641))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 399, 639))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.ShowRiskFunctionTableView = QtWidgets.QTableView(self.scrollAreaWidgetContents_3)
        self.ShowRiskFunctionTableView.setGeometry(QtCore.QRect(0, 0, 401, 641))
        self.ShowRiskFunctionTableView.setObjectName("ShowRiskFunctionTableView")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.RiskFunctionShowTextEdit = QtWidgets.QPlainTextEdit(self.page_2)
        self.RiskFunctionShowTextEdit.setGeometry(QtCore.QRect(10, 680, 401, 61))
        self.RiskFunctionShowTextEdit.setObjectName("RiskFunctionShowTextEdit")
        self.stackedWidget.addWidget(self.page_2)
        self.FunctionPushButton = QtWidgets.QPushButton(comment)
        self.FunctionPushButton.setGeometry(QtCore.QRect(540, 20, 211, 41))
        self.FunctionPushButton.setObjectName("FunctionPushButton")
        self.RiskFunctionPushButton = QtWidgets.QPushButton(comment)
        self.RiskFunctionPushButton.setGeometry(QtCore.QRect(750, 20, 191, 41))
        self.RiskFunctionPushButton.setObjectName("RiskFunctionPushButton")

        self.retranslateUi(comment)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(comment)

    def retranslateUi(self, comment):
        _translate = QtCore.QCoreApplication.translate
        comment.setWindowTitle(_translate("comment", "Form"))
        self.FunctionPushButton.setText(_translate("comment", "函数关系树列表"))
        self.RiskFunctionPushButton.setText(_translate("comment", "风险函数列表"))

from UI.NewCodeEditor import NewCodeEditor
