import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument


class LineNumberArea(QtWidgets.QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor


    def sizeHint(self):
        return QtCore.QSize(self.editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.fillRect(self.rect(), QtGui.QColor('#000000'))
        painter.setPen(QtGui.QColor('#000000'))  # 设置边界颜色为黑色
        self.editor.line_number_area_paint_event(event)

class NewCodeEditor(QtWidgets.QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 添加自定义的初始化代码
        self.setStyleSheet("QTextEdit { padding: 0; margin: 0; line-height: 1; }")
        self.line_number_area = LineNumberArea(self)
        self.document().blockCountChanged.connect(self.update_line_number_area_width)
        self.textChanged.connect(lambda: self.update_line_number_area(self.rect(), 0))
        self.verticalScrollBar().valueChanged.connect(lambda dy: self.update_line_number_area(self.rect(), dy))
        self.update_line_number_area_width()


    def line_number_area_width(self):
        digits = 1
        max_value = max(1, self.document().blockCount())
        while max_value >= 10:
            max_value /= 10
            digits += 1
        space = 10 + self.fontMetrics().width('9') * digits
        return space

    def update_line_number_area_width(self):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(QtCore.QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height()))

    def line_number_area_paint_event(self, event):
        painter = QtGui.QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QtGui.QColor('#000000'))
        painter.fillRect(event.rect(), QtCore.Qt.lightGray)
        # painter.fillRect(event.rect(), QtCore.Qt.black)

        cursor = self.cursorForPosition(self.viewport().rect().topLeft())
        block = cursor.block()

        cursor = self.textCursor()
        cursor.movePosition(QtGui.QTextCursor.Start)
        cursor.movePosition(QtGui.QTextCursor.Down, QtGui.QTextCursor.MoveAnchor, block.blockNumber())
        block_rect = self.cursorRect(cursor)
        top = block_rect.top()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and block_rect.bottom() >= event.rect().top():
                number = str(block.blockNumber() + 1)
                painter.setPen(QtCore.Qt.black)

                painter.drawText(0, top, self.line_number_area.width(), self.fontMetrics().height(),
                                 QtCore.Qt.AlignRight, number)

            block = block.next()
            cursor.movePosition(QtGui.QTextCursor.Down)
            block_rect = self.cursorRect(cursor)
            top = block_rect.top()

