import subprocess
import os
def run_cmd(cmd_list):
    """
    @description: 运行命令行代码，获取输出结果，其中输入为列表
    @Time：2023/7/19 || 11:04 ||20324
    """
    if isinstance(cmd_list,list):
        try:
            result = subprocess.run(cmd_list, capture_output=True, text=True,encoding='utf-8')
            output = result.stderr
            # print(output)
            return output
        except subprocess.CalledProcessError as e:
            error_output = e.stderr
            exit(error_output)
    else:
        try:
            result = subprocess.run(cmd_list, capture_output=True, text=True, shell=True,encoding='utf-8')
            output = result.stderr
            print(output)
            return output
        except subprocess.CalledProcessError as e:
            error_output = e.stderr
            exit(error_output)

def get_FilePath_folder(folder_path):
    file_paths = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
    return file_paths


