import os
import sys
from PyQt5 import QtWidgets
from UI.Main import *
from UI.CodeEditor import *


def file_tree_clicked():
    treeview = ui.treeView
    code_text = ui.plainTextEdit
    # 策略双击槽函数
    index = treeview.currentIndex()
    model = index.model()  # 请注意这里可以获得model的对象
    item_path = model.filePath(index)
    if not os.path.isdir(item_path):
        try:
            with open(item_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                print(file_content)  # 在这里可以使用文件内容进行进一步的处理
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
    treeview.doubleClicked.connect(file_tree_clicked)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    set_file_tree(ui)

    MainWindow.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     import sys
#     from PyQt5 import QtWidgets
#
#     app = QtWidgets.QApplication(sys.argv)
#     window = CodeEditor()
#     window.show()
#     sys.exit(app.exec_())

