"""
@FileName：fileTree.py
@Description:
@Time：2023/7/10 15:28
@user: 20324
"""
import os

from PyQt5.QtWidgets import  QTreeWidgetItem
from PyQt5.QtCore import QModelIndex
from PyQt5 import QtWidgets, QtCore
from detect.crawler import File
class FileTree:
    def __init__(self):
        self.file_path=""
    def open_folder_dialog(self,ui):
        folder_dialog = QtWidgets.QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(ui.treeView, "选择文件夹", 'D:/project_code/c/kaoyan')
        # 进行过滤并显示文件
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.rootPath())
        # 设置文件树模型的根节点
        ui.treeView.setModel(model)
        ui.treeView.setRootIndex(model.index(folder_path))
        self.file_path=folder_path
        ui.comboBox.setVisible(True)
    def display_filtered_files(self,ui):
        filter_list = ui.comboBox.currentText().split(',') #获取当前选择的过滤规则
        folder_path=self.file_path
        if folder_path:
            # 创建文件树模型
            model = QtWidgets.QFileSystemModel()
            model.setRootPath(QtCore.QDir.rootPath())
            # 设置过滤规则
            model.setNameFilters(filter_list)
            model.setNameFilterDisables(False)
            # 设置文件树模型的根节点
            ui.treeView.setModel(model)
            ui.treeView.setRootIndex(model.index(folder_path))
            # 遍历文件树，隐藏空的子文件夹
            root_index = model.index(folder_path)
            self.traverse_file_tree(ui,model,root_index)

    def traverse_file_tree(self,ui,model,index):
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
                ui.treeView.setRowHidden(child_index.row(), index, True)
            self.traverse_file_tree(ui,model, child_index)

    def prase_file_data(self,ui):
        treeview = ui.treeView
        index = treeview.currentIndex()
        model = index.model()  # 请注意这里可以获得model的对象
        # 获取根节点的索引
        root_index = QModelIndex()
        # 遍历根节点下的所有文件节点
        for row in range(model.rowCount(root_index)):
            file_index = model.index(row, 0, root_index)
            file_name = model.fileName(file_index)
            file = File(file_name)
            file.parse_c_file()
            # 将变量节点添加到文件节点下
            for variable in file.var_list:
                variable_node = QTreeWidgetItem(ui.treeView, [variable.name, variable.type])
                ui.treeView.setItemWidget(variable_node, 0, QTreeWidgetItem([variable.name, variable.type]))