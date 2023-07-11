import os
from UI.Main import *
import sys
from fileTree import FileTree
def file_tree_clicked():
    treeview = ui.treeView
    code_text = ui.plainTextEdit
    # 策略双击槽函数
    index = treeview.currentIndex()
    model = index.model()  # 请注意这里可以获得model的对象
    item_path = model.filePath(index)
    if not os.path.isdir(item_path):
        try:
            with open(item_path, 'r', encoding='gbk') as file:
                file_content = file.read()
                # print(file_content)  # 在这里可以使用文件内容进行进一步的处理
                code_text.setPlainText(file_content)
        except FileNotFoundError:
            print("文件不存在")
        except IOError:
            print("无法读取文件")

def set_file_tree(ui):
    model = QtWidgets.QFileSystemModel()
    model.setRootPath(QtCore.QDir.rootPath())
    model.setReadOnly(False)
    treeview = ui.treeView
    treeview.setModel(model)
    treeview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    treeview.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
    treeview.setHeaderHidden(True)
    treeview.hideColumn(1)
    treeview.hideColumn(2)
    treeview.hideColumn(3)
    #信号  槽部分
    treeview.doubleClicked.connect(file_tree_clicked)


def Groove_signal():
    """
    @description: 消息  槽的连接
    @Time：2023/7/11 || 10:00 ||20324
    """
    ui.action.triggered.connect(lambda: file_node.open_folder_dialog(ui)) #打开文件夹操作
    ui.comboBox.activated.connect(lambda: file_node.display_filtered_files(ui))

def Property_fun():
    """
    @description: 控件初始化
    @Time：2023/7/11 || 10:00 ||20324
    """
    ui.comboBox.setVisible(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    file_node = FileTree()#文件树操作对象
    #
    Groove_signal()  #槽函数与消息连接封装
    Property_fun()
    set_file_tree(ui)
    #
    MainWindow.show()
    sys.exit(app.exec_())


