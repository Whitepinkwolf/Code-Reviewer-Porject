from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QColor, QTextCharFormat, QTextDocument
from PyQt5.QtWidgets import QPlainTextEdit, QTextEdit

from UI.FindDialog import *
from UI.Main import *


class FindDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.find_text)
        self.ui.pb_next.clicked.connect(self.find_text_onebyone)
        self.sign = True
        self.current_index = 0  # 当前匹配字符串的索引位置

    def find_text(self):
        search_text = self.ui.lineEdit.text()
        if search_text:
            main_window = self.parent
            if isinstance(main_window, QtWidgets.QWidget):
                text_edit = main_window.findChild(QTextEdit, 'commentCodeEditor')
                self.highlight_text(text_edit, search_text)

    def highlight_text(self, plain_text_edit, search_text):
        cursor = plain_text_edit.textCursor()
        format = QTextCharFormat()
        format.setBackground(QColor("yellow"))

        extra_selections = []
        plain_text_edit.moveCursor(QTextCursor.Start)

        while cursor.hasComplexSelection() or cursor.atEnd() == False:
            cursor = plain_text_edit.document().find(search_text, cursor)

            if cursor.isNull() == False:
                selection = QTextEdit.ExtraSelection()
                selection.format = format
                selection.cursor = QTextCursor(cursor)
                extra_selections.append(selection)
            else:
                break

        plain_text_edit.setExtraSelections(extra_selections)

    def find_text_onebyone(self):
        if self.sign:
            self.find_text()
            self.sign = False
        main_window = self.parent
        if isinstance(main_window, QtWidgets.QWidget):

            text_edit = main_window.findChild(QTextEdit, 'commentCodeEditor')
            selections = text_edit.extraSelections()
            if self.current_index == len(selections):
                self.current_index = 0  # 若已到达最后一个匹配字符串，则从第一个开始

            if self.current_index < len(selections):
                cursor = QTextCursor(selections[self.current_index].cursor)
                text_edit.setTextCursor(cursor)
                self.ui.label.setText(f"{self.current_index+1}/{len(selections)}")
                self.current_index += 1



def set_search_dialog(ui, MainWindow):
    ui.findAction.triggered.connect(lambda: show_find_dialog(MainWindow))

def show_find_dialog(MainWindow):
    dialog = FindDialog(parent=MainWindow)
    dialog.show()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     dialog = FindDialog()
#     dialog.show()
#     sys.exit(app.exec_())
