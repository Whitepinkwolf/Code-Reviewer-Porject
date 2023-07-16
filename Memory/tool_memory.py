import subprocess


class ToolMemoryChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.output = ''
        self.error = ''
        self.compile_output = ''
        self.compile_error = ''

    #需要提前调用ToolClang库中的run_compile，如果没有则调用下面的gcc
    #drmemory.exe D:\work1\c_test_file\test.exe
    def run(self):
        cmd = ['drmemory.exe', self.file_path.replace('.c', '.exe')]
        print(cmd)
        # 执行命令并捕获输出
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            output = result.stderr
            self.output = output
            print(self.output)
        except subprocess.CalledProcessError as e:
            error_output = e.stderr
            self.error = error_output
            print(self.error)

    #gcc -o D:\work1\c_test_file\test.exe D:\work1\c_test_file\test.c
    def run_gcc_compile(self):
        cmd = ['gcc', '-o', self.file_path.replace('.c', '.exe'), self.file_path]
        print(cmd)
        # 执行命令并捕获输出
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            output = result.stderr
            self.compile_output = output
            if self.compile_output == '':
                self.compile_output = self.compile_output + 'The program compiles successfully ( '+self.file_path+' )'
            print(self.output)
        except subprocess.CalledProcessError as e:
            error_output = e.stderr
            self.compile_error = error_output
            print(self.error)

if __name__ == '__main__':
    # #example
    c_file_path = 'D:/work1/c_test_file/test.c'
    tool_memory = ToolMemoryChecker(c_file_path)
    tool_memory.run_gcc_compile()
    tool_memory.run()