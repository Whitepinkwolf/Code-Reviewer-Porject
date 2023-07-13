from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QTextCharFormat, QColor, QTextCursor
from PyQt5.QtWidgets import QTextEdit
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from qtpy import QtWidgets
from UI.commentWidget import Ui_comment
from Utils import *
from Data.getdata import Getdata


class comment_Widget(QtWidgets.QWidget, Ui_comment):
    def __init__(self, parent=None):
        super(comment_Widget, self).__init__(parent)
        self.setupUi(self)

        self.current_index = 0
        self.pre_cursor = None
        self.cursor = None

        self.initUI()
        self.connectSignalsSlots()

    def initUI(self):
        self.stackedWidget.setCurrentIndex(0)

    def connectSignalsSlots(self):
        self.FunctionPushButton.clicked.connect(self.on_pushButton1_clicked)
        self.RiskFunctionPushButton.clicked.connect(self.on_pushButton2_clicked)
        # 设置双击事件
        self.ShowDefineTableView.doubleClicked.connect(self.tableview_double_clicked)
        self.ShowRiskFunctionTableView.doubleClicked.connect(self.tableview_double_clicked)

    def on_pushButton1_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_pushButton2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

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
            data.append(item[0])
            data.append(header_file_str)
            data.append(str(item[1]))
            datas.append(data)
        for item in macro_definitions:
            data = []
            data.append(item[0])
            data.append(macro_definitions_str)
            data.append(str(item[1]))
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

    def set_RiskFunction_tableview(self):
        # 创建数据模型
        model = QStandardItemModel()
        # 设置列名称
        column_names = ['FunctionName', 'RiskLevel', 'Solution']
        model.setHorizontalHeaderLabels(column_names)

        # 添加数据
        datas = []

        for row in datas:
            item_row = []
            for item in row:
                item_cell = QStandardItem(item)
                item_cell.setEditable(False)  # 设置单元格不可编辑
                item_row.append(item_cell)
            model.appendRow(item_row)

        self.ShowRiskFunctionTableView.setModel(model)

    """
    bug
    """
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
            print(data)

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

            selections = code_text_new.extraSelections()
            self.current_index = 0
            print('selections length: ')
            print(len(selections))
            print('current_index: ')
            print(self.current_index)

            if self.current_index < len(selections):
                self.cursor = QTextCursor(selections[self.current_index].cursor)
                code_text_new.setTextCursor(self.cursor)
                self.current_index += 1

                if self.pre_cursor is not None:
                    # 设置行的格式
                    format = self.pre_cursor.blockFormat()
                    format.setBackground(QColor("#FFFFFF"))
                    self.pre_cursor.setBlockFormat(format)
                    # 将光标设置为初始位置
                    self.pre_cursor.movePosition(QTextCursor.StartOfBlock)
                    self.pre_cursor.setPosition(self.pre_cursor.position() + len(self.pre_cursor.block().text()),
                                                QTextCursor.KeepAnchor)

                line_number = self.cursor.blockNumber()

                if int(line) == line_number+1:
                    # 设置行的格式
                    format = self.cursor.blockFormat()
                    format.setBackground(QColor("red"))
                    self.cursor.setBlockFormat(format)

                    # 将光标设置为初始位置
                    self.cursor.movePosition(QTextCursor.StartOfBlock)
                    self.cursor.setPosition(self.cursor.position() + len(self.cursor.block().text()), QTextCursor.KeepAnchor)
                self.pre_cursor = self.cursor

    def set_open_text(self, item_path):
        getdata = Getdata(item_path)
        getdata.get_file_info_pre()
        getdata.get_local_info()
        file_content, header_files, macro_definitions, variable_names, function_declarations = getdata.get_all_local_data()

        # 设置tableview中的内容
        self.set_c_file_tableview(header_files, macro_definitions, variable_names, function_declarations)
        # self.set_RiskFunction_tableview

        # 设置editor中的内容
        lexer = get_lexer_by_name('c')
        formatter = HtmlFormatter(style='xcode')
        # 获取样式定义并嵌入到 HTML 代码中
        css_style = formatter.get_style_defs('.highlight')
        highlighted_code = highlight(file_content, lexer, formatter)
        html_code = f'<style>{css_style}</style>{highlighted_code}'
        self.commentCodeEditor.setHtml(html_code)

    def get_code_text(self):
        return self.commentCodeEditor.toPlainText()