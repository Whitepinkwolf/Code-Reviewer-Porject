import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI.Main import Ui_MainWindow
from UI.commentWidget import Ui_comment


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.set_file_tree()

        self.commentWidget = None  # 添加该行

    def connectSignalsSlots(self):
        self.treeView.doubleClicked.connect(self.file_tree_clicked)

    def file_tree_clicked(self):

        # 策略双击槽函数
        index = self.treeView.currentIndex()
        model = index.model()  # 请注意这里可以获得model的对象

        item_path = model.filePath(index)

        if not os.path.isdir(item_path):
            self.add_CommentWidget(item_path)
            try:
                with open(item_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    print(file_content)  # 在这里可以使用文件内容进行进一步的处理
                    self.commentWidget.plainTextEdit.setPlainText(file_content)
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

class comment_Widget(QtWidgets.QWidget, Ui_comment):
    def __init__(self, parent=None):
        super(comment_Widget, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())