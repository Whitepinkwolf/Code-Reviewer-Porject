from PyQt5 import QtWidgets
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from UI.extentDetect.MutiWidegt import Ui_MutiWidget
from Data import *


class mutiComment_Widget(QtWidgets.QWidget, Ui_MutiWidget):
    def __init__(self, parent=None):
        super(mutiComment_Widget, self).__init__(parent)
        self.setupUi(self)

        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pb_log.clicked.connect(self.on_pushButton1_clicked)
        self.pb_cmd.clicked.connect(self.on_pushButton2_clicked)

        # self.pb_compile.clicked.connect(self.xx)
        # self.pb_format.clicked.connect(self.xx)
        # self.pb_run.clicked.connect(self.xx)


    def on_pushButton1_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_pushButton2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    # # 新增tab
    # def add_extent_CommentWidget(self, item_path):

    def muti_set_open_text(self, item_path):
        getdata = Getdata(item_path)
        getdata.get_file_info_pre()
        getdata.get_local_info()
        file_content, header_files, macro_definitions, variable_names, function_declarations = getdata.get_all_local_data()

        # 设置editor中的内容
        file_content = file_content + '\n' + '//' + item_path
        lexer = get_lexer_by_name('c')
        formatter = HtmlFormatter(style='xcode')
        # 获取样式定义并嵌入到 HTML 代码中
        css_style = formatter.get_style_defs('.highlight')
        highlighted_code = highlight(file_content, lexer, formatter)
        html_code = f'<style>{css_style}</style>{highlighted_code}'
        self.CodeEditor.setHtml(html_code)

    def muti_get_code_text(self):
        return self.CodeEditor.toPlainText()




