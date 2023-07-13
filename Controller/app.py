import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from UI.Main import Ui_MainWindow
from commentWidget import comment_Widget
from fileTree import FileTree, index_get_path
from FindDialogController import FindDialog, set_search_dialog, show_find_dialog


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

        self.file_path = ''
        self.datas = []

        self.fileTree = FileTree(self)

        self.connectSignalsSlots()

        self.Property_fun()
        self.set_file_tree()

        self.commentWidget = None  # 添加该行
        self.findDialog = None

    def get_selected_items(self, model):
        self.datas.clear()
        selected_indexes = self.treeView.selectedIndexes()
        for index in selected_indexes:
            selected_file_path = model.filePath(index)
            selected_file_name = index.data()
            selected_file_directory = os.path.dirname(selected_file_path)
            self.datas.append(selected_file_path)
            self.datas.append(selected_file_name)
            self.datas.append(selected_file_directory)



    def show_save_another_dialog(self):
        selected_file_path, selected_file_name, selected_file_directory = self.datas[0], self.datas[1], self.datas[2]
        file_content = self.commentWidget.get_code_text()

        save_file_dir = selected_file_directory
        print(save_file_dir)
        save_path, _ = QFileDialog.getSaveFileName(None, "另存为", selected_file_directory + '/' + 'untitle.c',
                                                   "All Files (*);;C Files (*.c);;C header Files (*.h)")
        if save_path:
            # 打开文件并写入内容
            with open(save_path, 'w') as file:
                file.write(file_content)
            # 在这里可以执行保存文件的操作，比如将文件保存到 save_path 路径下
            print("保存路径:", save_path)


    def show_save_dialog(self):
        selected_file_path, selected_file_name, selected_file_directory = self.datas[0], self.datas[1], self.datas[2]
        file_content = self.commentWidget.get_code_text()
        save_file_dir = selected_file_path
        print(save_file_dir)
        print(1)
        if save_file_dir:
            # 打开文件并写入内容
            with open(save_file_dir, 'w') as file:
                file.write(file_content)
            # 在这里可以执行保存文件的操作，比如将文件保存到 save_path 路径下
            print("保存路径:", save_file_dir)

    def connectSignalsSlots(self):
        self.treeView.doubleClicked.connect(self.file_tree_clicked)

        self.openAction.triggered.connect(self.fileTree.open_folder_dialog)  # 打开文件夹操作
        self.ChooseComboBox.activated.connect(self.fileTree.display_filtered_files)
        # self.openAction.triggered.connect(self.open_folder_dialog)  # 打开文件夹操作
        # self.ChooseComboBox.activated.connect(self.display_filtered_files)

        self.findAction.triggered.connect(self.show_find_dialog)

        self.saveAction.triggered.connect(lambda: self.show_save_dialog())
        self.saveAsAction.triggered.connect(lambda: self.show_save_another_dialog())


    def show_find_dialog(self):
        # commentWidget = comment_Widget()
        # self.commentTabWidget.addTab(commentWidget, item_path)
        #
        # self.commentWidget = commentWidget  # 添加该行

        self.findDialog = FindDialog(self.commentWidget)
        self.findDialog.show()

    def file_tree_clicked(self):
        model = self.treeView.model()
        if isinstance(model, QtWidgets.QFileSystemModel):
            index = self.treeView.currentIndex()
            item_path = index.model().filePath(index)
        elif isinstance(model, QtGui.QStandardItemModel):
            # 策略双击槽函数
            item_path = index_get_path(self)[0]

        if not os.path.isdir(item_path):
            self.add_CommentWidget(item_path)
            try:
                with open(item_path, 'r', encoding='gbk') as file:
                    file_content = file.read()
                     # 在这里可以使用文件内容进行进一步的处理

                    self.commentWidget.set_open_text(item_path)

            except FileNotFoundError:
                print("文件不存在")
            except IOError:
                print("无法读取文件")

    def add_CommentWidget(self, item_path):
        commentWidget = comment_Widget()
        self.commentTabWidget.addTab(commentWidget, item_path)

        self.commentWidget = commentWidget  # 添加该行

    def set_file_tree(self):
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.rootPath())
        model.setReadOnly(False)
        self.treeView.setModel(model)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeView.setHeaderHidden(True)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.selectionModel().selectionChanged.connect(lambda: self.get_selected_items(model))

    def Property_fun(self):
        """
        @description: 控件初始化
        @Time：2023/7/11 || 10:00 ||20324
        """
        self.ChooseComboBox.setVisible(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())