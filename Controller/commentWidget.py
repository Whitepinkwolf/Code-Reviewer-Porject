from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QTextCharFormat, QColor, QTextCursor
from PyQt5.QtWidgets import QTextEdit
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from qtpy import QtWidgets
from UI.commentWidget import Ui_comment
from Utils import *
from getdata import Getdata


class comment_Widget(QtWidgets.QWidget, Ui_comment):
    def __init__(self, parent=None):
        super(comment_Widget, self).__init__(parent)
        self.setupUi(self)

        # 设置双击事件
        self.ShowDefineTableView.doubleClicked.connect(self.tableview_double_clicked)

    def set_c_file_tableview(self, header_files, macro_definitions, variable_names, function_declarations):

        # 创建数据模型
        model = QStandardItemModel()
        # 设置列名称
        column_names = ['Name', 'Type', 'Line']
        model.setHorizontalHeaderLabels(column_names)

        # 添加数据
        datas = []

        for item in header_files:
            data = []
            data.append(item)
            data.append(header_file_str)
            data.append('\\')
            datas.append(data)
        for item in macro_definitions:
            data = []
            data.append(item)
            data.append(macro_definitions_str)
            data.append('\\')
            datas.append(data)
        for item in variable_names:
            data = []
            data.append(item[0])
            data.append(item[1])
            data.append(str(item[2]))
            datas.append(data)
        for item in function_declarations:
            data = []
            data.append(item[0])
            data.append(item[1])
            data.append(str(item[2]))
            datas.append(data)

        for row in datas:
            item_row = []
            for item in row:
                item_cell = QStandardItem(item)
                item_cell.setEditable(False)  # 设置单元格不可编辑
                item_row.append(item_cell)
            model.appendRow(item_row)

        self.ShowDefineTableView.setModel(model)

    def tableview_double_clicked(self, index):
        tableview = self.ShowDefineTableView
        pte_content = self.ShowTextEdit
        code_text_new = self.commentCodeEditor
        if index.isValid():
            index_row = index.row()
            index_column = index.column()
            value = index.data()
            print(f"Double clicked on item: row={index_row}, column={index_column}, item={value}")
            pte_content.setPlainText(value)

            # 获取行数据
            model = tableview.model()
            data = []
            for column in range(model.columnCount()):
                item = model.index(index_row, column).data(Qt.DisplayRole)
                data.append(item)
            line = data[2]
            # print(data)

            if index_column == 0:
                search_text = value
                cursor = code_text_new.textCursor()
                format = QTextCharFormat()
                format.setBackground(QColor("yellow"))

                extra_selections = []
                code_text_new.moveCursor(QTextCursor.Start)

                while cursor.hasComplexSelection() or cursor.atEnd() == False:
                    cursor = code_text_new.document().find(search_text, cursor)

                    if cursor.isNull() == False:
                        target_number = cursor.block().blockNumber() + 1
                        if str(target_number) == line:
                            selection = QTextEdit.ExtraSelection()
                            selection.format = format
                            selection.cursor = QTextCursor(cursor)
                            extra_selections.append(selection)
                    else:
                        break
                code_text_new.setExtraSelections(extra_selections)
            elif (line != '\\'):
                target_text = data[0]
                # 获取总行数
                total_lines = code_text_new.document().blockCount()
                # 设置高亮格式
                format = QTextCharFormat()
                format.setBackground(QColor("yellow"))
                # 添加高亮选择
                extra_selections = []

                if int(line) <= total_lines:
                    target_line = int(line) - 1
                    block = code_text_new.document().findBlockByLineNumber(target_line)
                    if block.isValid():
                        # 获取目标行的文本
                        line_text = block.text()
                        # 在目标行中查找目标字符串的位置
                        index = line_text.find(target_text)
                        while index != -1:
                            # 创建额外选择并设置高亮
                            cursor = QTextCursor(block)
                            cursor.setPosition(block.position() + index)
                            cursor.setPosition(block.position() + index + len(target_text), QTextCursor.KeepAnchor)
                            selection = QTextEdit.ExtraSelection()
                            selection.format = format
                            selection.cursor = cursor
                            extra_selections.append(selection)
                            # 在目标行中继续查找下一个目标字符串的位置
                            index = line_text.find(target_text, index + len(target_text))

                code_text_new.setExtraSelections(extra_selections)

    def set_open_text(self, item_path):
        getdata = Getdata(item_path)
        getdata.get_file_info_pre()
        getdata.get_local_info()
        file_content, header_files, macro_definitions, variable_names, function_declarations = getdata.get_all_local_data()
        self.set_c_file_tableview(header_files, macro_definitions, variable_names, function_declarations)

        """
        还没有颜色
        """
        lexer = get_lexer_by_name('c')
        formatter = HtmlFormatter(style='xcode')
        # 获取样式定义并嵌入到 HTML 代码中
        css_style = formatter.get_style_defs('.highlight')
        highlighted_code = highlight(file_content, lexer, formatter)
        html_code = f'<style>{css_style}</style>{highlighted_code}'
        self.commentCodeEditor.setHtml(html_code)