import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI.Main import Ui_MainWindow
from commentWidget import comment_Widget
from fileTree import FileTree
from FindDialogController import FindDialog, set_search_dialog, show_find_dialog


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

        self.file_path = ''
        self.fileTree = FileTree()

        self.connectSignalsSlots()

        self.Property_fun()
        self.set_file_tree()

        self.commentWidget = None  # 添加该行
        self.findDialog = None

    def connectSignalsSlots(self):
        self.treeView.doubleClicked.connect(self.file_tree_clicked)

        # self.openAction.triggered.connect(self.fileTree.open_folder_dialog(Ui_MainWindow()))  # 打开文件夹操作
        # self.ChooseComboBox.activated.connect(self.fileTree.display_filtered_files(Ui_MainWindow()))
        self.openAction.triggered.connect(self.open_folder_dialog)  # 打开文件夹操作
        self.ChooseComboBox.activated.connect(self.display_filtered_files)

        self.findAction.triggered.connect(self.show_find_dialog)


    def show_find_dialog(self):
        # commentWidget = comment_Widget()
        # self.commentTabWidget.addTab(commentWidget, item_path)
        #
        # self.commentWidget = commentWidget  # 添加该行

        self.findDialog = FindDialog(self.commentWidget)
        self.findDialog.show()

    def open_folder_dialog(self):
        folder_dialog = QtWidgets.QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(self.treeView, "选择文件夹")
        # 进行过滤并显示文件
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.rootPath())
        # 设置文件树模型的根节点
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(folder_path))
        self.file_path = folder_path
        self.ChooseComboBox.setVisible(True)

    def display_filtered_files(self):
        filter_list = self.ChooseComboBox.currentText().split(',') #获取当前选择的过滤规则
        folder_path = self.file_path
        if folder_path:
            # 创建文件树模型
            model = QtWidgets.QFileSystemModel()
            model.setRootPath(QtCore.QDir.rootPath())
            # 设置过滤规则
            model.setNameFilters(filter_list)
            model.setNameFilterDisables(False)
            # 设置文件树模型的根节点
            self.treeView.setModel(model)
            self.treeView.setRootIndex(model.index(folder_path))
            # 遍历文件树，隐藏空的子文件夹
            root_index = model.index(folder_path)
            self.traverse_file_tree(model, root_index)

    def traverse_file_tree(self, model, index):
        # 递归去除重复文件
        if not index.isValid():
            return
        # 获取子文件夹列表
        dir_path = model.filePath(index)
        subfolders = QtCore.QDir(dir_path).entryList(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        # 遍历子文件夹
        for subfolder in subfolders:
            subfolder_path = os.path.join(dir_path, subfolder)
            files_in_folder = [file for file in os.listdir(subfolder_path) if
                               os.path.isfile(os.path.join(subfolder_path, file))]
            child_index = model.index(os.path.join(dir_path, subfolder))
            if not files_in_folder:
                # 子文件夹为空，隐藏该子文件夹
                self.treeView.setRowHidden(child_index.row(), index, True)
            self.traverse_file_tree(model, child_index)

    def file_tree_clicked(self):

        # 策略双击槽函数
        index = self.treeView.currentIndex()
        model = index.model()  # 请注意这里可以获得model的对象

        item_path = model.filePath(index)

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