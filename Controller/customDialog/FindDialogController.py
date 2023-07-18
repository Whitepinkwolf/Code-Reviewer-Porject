from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QTextCursor, QColor, QTextCharFormat
from PyQt5.QtWidgets import QTextEdit

from UI.Dialog.FindDialog import *
from UI.Main import *


class FindDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.ui = Ui_FindDialog()
        self.ui.setupUi(self)

        self.initUI()

        self.sign = True
        self.current_index = 0  # 当前匹配字符串的索引位置
        self.connectSignalsSlots()

    def initUI(self):
        self.ui.ReCheckBox.setChecked(True)
        self.ui.ReCheckBox.setEnabled(False)
        self.ui.IgonreCheckBox.setChecked(True)
        self.ui.IgonreCheckBox.setEnabled(False)

    def connectSignalsSlots(self):
        self.ui.FindPushButton.clicked.connect(self.find_text)
        self.ui.FindNextPushButton.clicked.connect(self.find_text_onebyone)

    def find_text(self):
        search_text = self.ui.FindLineEdit.text()
        if search_text:
            main_window = self.parent
            if isinstance(main_window, QtWidgets.QWidget):
                text_edit = main_window.findChild(QTextEdit, 'commentCodeEditor')
                self.highlight_text(text_edit, search_text)

    def highlight_text(self, plain_text_edit, search_text):
        # cursor = plain_text_edit.textCursor()
        format = QTextCharFormat()
        format.setBackground(QColor("yellow"))

        extra_selections = []
        plain_text_edit.moveCursor(QTextCursor.Start)
        cursor = plain_text_edit.textCursor()

        while cursor.hasComplexSelection() or cursor.atEnd() == False:
            # cursor = plain_text_edit.document().find(search_text, cursor)
            regex = QRegularExpression(search_text)
            cursor = plain_text_edit.document().find(regex, cursor)

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

                # 设置行的格式
                format = cursor.blockFormat()
                format.setBackground(QColor("blue"))
                cursor.setBlockFormat(format)
                # 将光标设置为初始位置
                cursor.movePosition(QTextCursor.StartOfBlock)
                cursor.setPosition(cursor.position() + len(cursor.block().text()), QTextCursor.KeepAnchor)
                line_number = cursor.blockNumber()

                if self.current_index > 0:
                    previous_cursor = QTextCursor(selections[self.current_index - 1].cursor)
                    pre_line_number = previous_cursor.blockNumber()
                    if line_number != pre_line_number:
                        # 设置行的格式
                        format = cursor.blockFormat()
                        format.setBackground(QColor("#FFFFFF"))
                        previous_cursor.setBlockFormat(format)
                        # 将光标设置为初始位置
                        previous_cursor.movePosition(QTextCursor.StartOfBlock)
                        previous_cursor.setPosition(previous_cursor.position() + len(previous_cursor.block().text()),
                                                    QTextCursor.KeepAnchor)

                # 滚动到显示匹配字符串的行
                text_edit.ensureCursorVisible()

                self.ui.label.setText(f"{self.current_index + 1}/{len(selections)}")
                self.current_index += 1
