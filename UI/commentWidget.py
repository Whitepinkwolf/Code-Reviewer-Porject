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
        comment.resize(927, 761)
        self.plainTextEdit = CodeEditor(comment)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 1001, 891))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(comment)
        QtCore.QMetaObject.connectSlotsByName(comment)

    def retranslateUi(self, comment):
        _translate = QtCore.QCoreApplication.translate
        comment.setWindowTitle(_translate("comment", "Form"))

from UI.CodeEditor import CodeEditor
