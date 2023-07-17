from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QProcess, Qt
from PyQt5.QtGui import QTextCursor
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from Data import *
from Data.getdata import *
from UI.extentDetect.MutiWidget import Ui_MutiWidget
from Memory.tool_Clang import *
from Memory.tool_flawfinder import *
from Memory.tool_cppchecker import *
from Utils import *


class mutiComment_Widget(QtWidgets.QWidget, Ui_MutiWidget):
    def __init__(self, parent=None):
        super(mutiComment_Widget, self).__init__(parent)

        self.setupUi(self)
        self.file_path = None
        self.tool_clang = None
        self.tool_flawfinder = None
        self.tool_cppchecker = None

        self.process = QProcess()
        self.cmd()

        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.te_cmd.commandEntered.connect(self.execute_command)


    def cmd(self):
        self.te_cmd.setReadOnly(False)
        # 创建 QProcess 对象
        self.process.setProgram("cmd")
        # self.process.setWorkingDirectory("C:\\Users")
        # self.process.setProcessChannelMode(QProcess.MergedChannels)  # 将标准输出和标准错误合并
        # self.process.readyRead.connect(self.update_cmd)
        self.process.readyReadStandardOutput.connect(self.update_cmd)
        self.process.readyReadStandardError.connect(self.update_cmd)
        self.process.start("cmd")

    def update_cmd(self):
        while self.process.bytesAvailable():
            # 读取命令提示符的输出并将其追加到 QTextEdit 中
            # output = self.process.readAll().data()
            output = self.process.readAllStandardOutput().data()
            error = self.process.readAllStandardError().data()
            print(output)
            print(error)
            text = ""
            if output:
                try:
                    text = output.decode("utf-8")
                except UnicodeDecodeError:
                    text = output.decode("gbk", errors="replace")
                print(text)
                self.te_cmd.moveCursor(QTextCursor.End)
                self.te_cmd.insertPlainText(text)
                self.te_cmd.moveCursor(QTextCursor.End)
            if error:
                try:
                    text = error.decode("utf-8")
                except UnicodeDecodeError:
                    text = error.decode("gbk", errors="replace")
                print(text)
                self.te_cmd.moveCursor(QTextCursor.End)
                self.te_cmd.insertPlainText(text)
                self.te_cmd.moveCursor(QTextCursor.End)

    def execute_command(self, command):
        QtCore.QTimer.singleShot(100, lambda: self.process.write(f"{command}\n".encode()))
        self.process.waitForBytesWritten()  # 等待写入完成，确保命令被发送

    def init_tools(self, item_path):
        self.file_path = item_path
        self.tool_clang = ToolClang(self.file_path, get_available_llvm_path(llvm_path))
        self.tool_flawfinder = ToolFlawfinder(self.file_path)
        self.tool_cppchecker = ToolCppChecker(self.file_path)

        self.pb_compile.clicked.connect(lambda: self.compile_code())
        self.pb_format.clicked.connect(lambda: self.format_code())
        self.pb_run.clicked.connect(lambda: self.run_code())
        # 将动作与处理函数相关联
        self.pb_detect.actionA.triggered.connect(lambda: self.run_flawfinder_scan())
        self.pb_detect.actionB.triggered.connect(lambda: self.run_clang_tidy_scan())
        self.pb_detect.actionC.triggered.connect(lambda: self.run_clang_checker_scan())
        self.pb_detect.actionD.triggered.connect(lambda: self.run_clang_scan_build_scan())
        self.pb_detect.actionE.triggered.connect(lambda: self.run_cppchecker_scan())
        self.pb_detect.actionF.triggered.connect(lambda: self.run_code_evaluation())

    # def on_pushButton1_clicked(self):
    #     self.stackedWidget.setCurrentIndex(0)
    #
    # def on_pushButton2_clicked(self):
    #     self.stackedWidget.setCurrentIndex(1)

    # 新增tab
    def add_extent_CommentWidget(self):
        file_name = os.path.basename(item_path)

        # 检查是否已存在相同路径的tab
        for index in range(self.commentTabWidget.count()):
            tab_widget = self.commentTabWidget.widget(index)
            if tab_widget.property("FilePath") == item_path:
                # 切换到已存在的tab
                self.commentTabWidget.setCurrentWidget(tab_widget)
                return

        # 不存在相同路径的tab，新增tab
        mutiCommentWidget = mutiComment_Widget()
        self.commentTabWidget.addTab(mutiCommentWidget, file_name)
        mutiCommentWidget.setProperty("FilePath", item_path)

        self.mutiCommentWidget = mutiCommentWidget
        self.commentTabWidget.setCurrentWidget(mutiCommentWidget)

    #此部分的所有检测还未实现对应组件，因此仅仅是运行
    def run_flawfinder_scan(self):
        self.tool_flawfinder.run()
        self.tool_flawfinder.get_data()
        self.tool_flawfinder.get_graph_base_data()
        print(self.tool_flawfinder.result_text)
        # ...

    def run_clang_tidy_scan(self):
        self.tool_clang.run_static_scan()

    def run_clang_checker_scan(self):
        self.tool_clang.run_static_scan_strict()

    def run_clang_scan_build_scan(self):
        self.tool_clang.run_static_scan_report()

    def run_cppchecker_scan(self):
        self.tool_cppchecker.run_scan()

    def run_code_evaluation(self):
        self.tool_clang.run_code_quality_evaluation()

    def run_code(self):
        self.tool_clang.run_exec()
        message = 'stdout: ' + self.tool_clang.run_output+'\n'+'stderr: '+self.tool_clang.run_error
        self.te_log.setPlainText(message)

    def compile_code(self):
        self.tool_clang.run_compile()
        message = 'stdout: ' + self.tool_clang.compile_output+'\n'+'stderr: '+self.tool_clang.compile_error
        self.te_log.setPlainText(message)

    def format_code(self):
        self.tool_clang.format_code()
        message = 'stdout: ' + self.tool_clang.format_output+'\n'+'stderr: '+self.tool_clang.format_error
        self.te_log.setPlainText(message)


    def get_file_path(self):
        item_path = self.CodeEditor.toPlainText().splitlines()[-1].replace('//', '').replace(' ', '')
        return item_path

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

        self.init_tools(item_path)

    def muti_get_code_text(self):
        return self.CodeEditor.toPlainText()




