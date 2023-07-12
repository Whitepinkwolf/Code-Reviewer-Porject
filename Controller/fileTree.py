"""
@FileName：fileTree.py
@Description:
@Time：2023/7/10 15:28
@user: 20324
"""
import fnmatch
import os
from PyQt5 import QtWidgets
from Controller.crawler import File
from PyQt5.QtGui import QStandardItem, QStandardItemModel


def is_c_or_h_file(file_path):
    # 判断文件是否为C文件或头文件
    return file_path.endswith('.c') or file_path.endswith('.h')

def File_get(file_path):
    file_path = file_path.replace("/", "\\")
    file_obj=File(file_path)
    file_obj.parse_c_file()
    element_list=[]
    for function in file_obj.fun_list:
        element_list.append(function.combine_function())
    for struct in file_obj.struct_list:
        element_list.append(struct.name)
    for gobal_var in file_obj.var_list:
        element_list.append(gobal_var.name)
    return element_list

class FileTree:
    def __init__(self, ui):
        self.folder_path = ""
        self.ui=ui
        self.tree_view = ui.treeView  # 显示存储结构
        self.tree_model = QStandardItemModel()  # 存储的数据结构

    def open_folder_dialog(self):
        ui=self.ui
        folder_dialog = QtWidgets.QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(ui.treeView, "选择文件夹", 'D:\project_code\pythonproject\CodeAuditing\\test_c')
        self.tree_model.clear()  # 清空现有的模型数据
        self.folder_path = folder_path
        ui.comboBox.setVisible(True)
        # 添加根节点
        root_item = QStandardItem(folder_path)
        self.tree_model.appendRow(root_item)
        # 遍历文件夹并添加到根节点
        self.add_folder_to_node(folder_path, root_item)
        self.tree_view.setModel(self.tree_model)
        self.tree_view.expandToDepth(0)

    def add_folder_to_node(self, folder_path, parent_item):#添加文件夹
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isdir(file_path):
                folder_item = QStandardItem(file_name)
                parent_item.appendRow(folder_item)
                self.add_folder_to_node(file_path, folder_item)

            elif os.path.isfile(file_path):
                file_item = QStandardItem(file_name)
                parent_item.appendRow(file_item)
                self.add_element_to_node(file_path, file_item)

    def add_element_to_node(self, file_path, parent_item):
        elements = File_get(file_path)
        for element in elements:
            function_item = QStandardItem(element)
            parent_item.appendRow(function_item)

    def display_filtered_files(self):
        folder_path=self.folder_path
        self.tree_model.clear()  # 清空现有的模型数据
        # 添加根节点
        root_item = QStandardItem(folder_path)
        self.tree_model.appendRow(root_item)
        # 遍历文件夹并添加到根节点
        self.add_folder_to_node(folder_path, root_item)
        self.tree_view.setModel(self.tree_model)
        root_item = self.tree_model.item(0)  # 获取根节点
        if root_item:# 遍历文件树，设置显示/隐藏属性
            self.remove_filtered_files(root_item)

        self.tree_view.expandToDepth(0)

    def remove_filtered_files(self, parent_item):
        for row in reversed(range(parent_item.rowCount())):
            item = parent_item.child(row)
            if item.hasChildren():
                self.remove_filtered_files(item)
                if item.rowCount() == 0:
                    parent_item.removeRow(row)
            else:
                file_path = os.path.join(self.folder_path, item.text())
                if  not self.is_file_match_filter(file_path):
                    parent_item.removeRow(row)

    def is_file_match_filter(self, file_path): #匹配筛选条件
        filter_list = self.ui.comboBox.currentText().split(',')  # 获取当前选择的过滤规则
        file_name = os.path.basename(file_path)
        return any(fnmatch.fnmatch(file_name, filter_pattern) for filter_pattern in filter_list)
