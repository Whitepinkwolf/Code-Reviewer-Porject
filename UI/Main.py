# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1288, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 0, 281, 791))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 789))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeView = QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.treeView.setGeometry(QtCore.QRect(10, 40, 251, 731))
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
        self.commentTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.commentTabWidget.setGeometry(QtCore.QRect(330, 0, 931, 791))
        self.commentTabWidget.setObjectName("commentTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit = CodeEditor(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(-70, -120, 1001, 891))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.commentTabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1288, 26))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.saveAction = QtWidgets.QAction(MainWindow)
        self.saveAction.setObjectName("saveAction")
        self.saveAsAction = QtWidgets.QAction(MainWindow)
        self.saveAsAction.setObjectName("saveAsAction")
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.findAction = QtWidgets.QAction(MainWindow)
        self.findAction.setObjectName("findAction")
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.findAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveAsAction)
        self.fileMenu.addAction(self.exitAction)
        self.menubar.addAction(self.fileMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.commentTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "文件目录"))
        self.ChooseComboBox.setItemText(0, _translate("MainWindow", "*"))
        self.ChooseComboBox.setItemText(1, _translate("MainWindow", "*.c"))
        self.ChooseComboBox.setItemText(2, _translate("MainWindow", "*.h"))
        self.ChooseComboBox.setItemText(3, _translate("MainWindow", "*.c,*.h"))
        self.commentTabWidget.setTabText(self.commentTabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.fileMenu.setTitle(_translate("MainWindow", "文件"))
        self.openAction.setText(_translate("MainWindow", "打开"))
        self.saveAction.setText(_translate("MainWindow", "保存"))
        self.saveAsAction.setText(_translate("MainWindow", "另存为"))
        self.exitAction.setText(_translate("MainWindow", "退出"))
        self.findAction.setText(_translate("MainWindow", "查找"))

from UI.CodeEditor import CodeEditor
