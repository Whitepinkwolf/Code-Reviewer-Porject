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
        ManageRiskFunction.resize(1333, 863)
        self.AllRiskFuncTableWidget = QtWidgets.QTableWidget(ManageRiskFunction)
        self.AllRiskFuncTableWidget.setGeometry(QtCore.QRect(30, 120, 1261, 721))
        self.AllRiskFuncTableWidget.setStyleSheet("QTableWidget::horizontalHeader {\n"
"    background-color: #98b4d5;\n"
"}\n"
"")
        self.AllRiskFuncTableWidget.setGridStyle(QtCore.Qt.SolidLine)
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
        self.AllRiskFuncTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.DeletePushButton = QtWidgets.QPushButton(ManageRiskFunction)
        self.DeletePushButton.setGeometry(QtCore.QRect(230, 50, 111, 41))
        self.DeletePushButton.setObjectName("DeletePushButton")
        self.AddPushButton = QtWidgets.QPushButton(ManageRiskFunction)
        self.AddPushButton.setGeometry(QtCore.QRect(90, 50, 111, 41))
        self.AddPushButton.setObjectName("AddPushButton")
        self.FindTextEdit = QtWidgets.QTextEdit(ManageRiskFunction)
        self.FindTextEdit.setGeometry(QtCore.QRect(440, 50, 621, 41))
        self.FindTextEdit.setObjectName("FindTextEdit")
        self.FindPushButton = QtWidgets.QPushButton(ManageRiskFunction)
        self.FindPushButton.setGeometry(QtCore.QRect(1090, 50, 111, 41))
        self.FindPushButton.setObjectName("FindPushButton")
        self.picLable = QtWidgets.QLabel(ManageRiskFunction)
        self.picLable.setGeometry(QtCore.QRect(400, 50, 41, 41))
        self.picLable.setText("")
        self.picLable.setObjectName("picLable")
        self.picLable2 = ClickableLabel(ManageRiskFunction)
        self.picLable2.setGeometry(QtCore.QRect(1020, 50, 41, 41))
        self.picLable2.setText("")
        self.picLable2.setObjectName("picLable2")

        self.retranslateUi(ManageRiskFunction)
        QtCore.QMetaObject.connectSlotsByName(ManageRiskFunction)

    def retranslateUi(self, ManageRiskFunction):
        _translate = QtCore.QCoreApplication.translate
        ManageRiskFunction.setWindowTitle(_translate("ManageRiskFunction", "Form"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(0)
        item.setWhatsThis(_translate("ManageRiskFunction", "QCheckBox"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageRiskFunction", "FunctionName"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManageRiskFunction", "RiskLevel"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManageRiskFunction", "Solution"))
        self.DeletePushButton.setText(_translate("ManageRiskFunction", "删除"))
        self.AddPushButton.setText(_translate("ManageRiskFunction", "新增"))
        self.FindPushButton.setText(_translate("ManageRiskFunction", "查找"))

from UI.ToolWidget.ClickableLabel import ClickableLabel
