import subprocess


class ToolMemoryChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.output = ''
        self.error = ''

    #需要提前调用ToolClang库中的run_compile
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

if __name__ == '__main__':
    # #example
    c_file_path = 'D:/work1/c_test_file/test.c'
    tool_memory = ToolMemoryChecker(c_file_path)
    tool_memory.run()