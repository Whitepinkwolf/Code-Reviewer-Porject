# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageRiskFunctionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManageRiskFunction(object):
    def setupUi(self, ManageRiskFunction):
        ManageRiskFunction.setObjectName("ManageRiskFunction")
        ManageRiskFunction.resize(1320, 881)
        self.AllRiskFuncTableWidget = QtWidgets.QTableWidget(ManageRiskFunction)
        self.AllRiskFuncTableWidget.setGeometry(QtCore.QRect(50, 150, 1231, 691))
        self.AllRiskFuncTableWidget.setObjectName("AllRiskFuncTableWidget")
        self.AllRiskFuncTableWidget.setColumnCount(4)
        self.AllRiskFuncTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.AllRiskFuncTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllRiskFuncTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllRiskFuncTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllRiskFuncTableWidget.setHorizontalHeaderItem(3, item)
        self.groupBox = QtWidgets.QGroupBox(ManageRiskFunction)
        self.groupBox.setGeometry(QtCore.QRect(370, 80, 841, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.graphicsView.setObjectName("graphicsView")
        self.FindPlainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.FindPlainTextEdit.setGeometry(QtCore.QRect(40, 0, 661, 41))
        self.FindPlainTextEdit.setObjectName("FindPlainTextEdit")
        self.FindPushButton = QtWidgets.QPushButton(self.groupBox)
        self.FindPushButton.setGeometry(QtCore.QRect(730, 0, 111, 41))
        self.FindPushButton.setObjectName("FindPushButton")
        self.DeletePushButton = QtWidgets.QPushButton(ManageRiskFunction)
        self.DeletePushButton.setGeometry(QtCore.QRect(220, 80, 111, 41))
        self.DeletePushButton.setObjectName("DeletePushButton")
        self.AddPushButton = QtWidgets.QPushButton(ManageRiskFunction)
        self.AddPushButton.setGeometry(QtCore.QRect(80, 80, 111, 41))
        self.AddPushButton.setObjectName("AddPushButton")

        self.retranslateUi(ManageRiskFunction)
        QtCore.QMetaObject.connectSlotsByName(ManageRiskFunction)

    def retranslateUi(self, ManageRiskFunction):
        _translate = QtCore.QCoreApplication.translate
        ManageRiskFunction.setWindowTitle(_translate("ManageRiskFunction", "Form"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ManageRiskFunction", " "))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageRiskFunction", "FunctionName"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManageRiskFunction", "RiskLevel"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManageRiskFunction", "Solution"))
        self.FindPushButton.setText(_translate("ManageRiskFunction", "查找"))
        self.DeletePushButton.setText(_translate("ManageRiskFunction", "删除"))
        self.AddPushButton.setText(_translate("ManageRiskFunction", "新增"))

