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
        comment.resize(966, 770)
        self.ShowTextEdit = QtWidgets.QPlainTextEdit(comment)
        self.ShowTextEdit.setGeometry(QtCore.QRect(550, 680, 381, 71))
        self.ShowTextEdit.setObjectName("ShowTextEdit")
        self.scrollArea_2 = QtWidgets.QScrollArea(comment)
        self.scrollArea_2.setGeometry(QtCore.QRect(540, 10, 411, 661))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 409, 659))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.ShowDefineTableView = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.ShowDefineTableView.setGeometry(QtCore.QRect(10, 10, 381, 631))
        self.ShowDefineTableView.setObjectName("ShowDefineTableView")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea = QtWidgets.QScrollArea(comment)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 511, 741))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 739))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.commentCodeEditor = NewCodeEditor(self.scrollAreaWidgetContents)
        self.commentCodeEditor.setGeometry(QtCore.QRect(10, 10, 491, 721))
        self.commentCodeEditor.setObjectName("commentCodeEditor")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(comment)
        QtCore.QMetaObject.connectSlotsByName(comment)

    def retranslateUi(self, comment):
        _translate = QtCore.QCoreApplication.translate
        comment.setWindowTitle(_translate("comment", "Form"))

from UI.NewCodeEditor import NewCodeEditor
