import os

header_file_str = 'Header file'
macro_definitions_str = 'Macro definition'
encoding_list=['utf-8', 'gbk'] #encoding列表
encoding_mode = 'gbk'
neu_copy_right = ' and Software College of Northeastern University'

#这个部分传入对应的llvm的路径，第一个是我的，剩下的需要你们自行添加
llvm_path = ['X:/llvm','D:/llvm','']


def get_available_llvm_path(llvm_path):
    for path in llvm_path:
        if os.path.exists(path):
            return path
    return None
def check_extension(item_path):
    file_extension = os.path.splitext(item_path)[1]
    if file_extension == '.c' or file_extension == '.h':
        return True
    else:
        return False

def get_debug_database():
    import os
    # 获取当前用户的临时文件夹路径
    temp_folder = os.path.join(os.path.expanduser("~"), 'AppData', 'Local', 'Temp')
    # 查找以'sqlmapipc-'开头的文件
    files = [f for f in os.listdir(temp_folder) if f.startswith('scan-build-')]
    # 获取最新创建的文件路径
    if files:
        latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(temp_folder, f)))
        db_path = os.path.join(temp_folder, latest_file)
        print(db_path)
        return db_path
    return

def open_with_encodings(file_path):
    """
    @description: 通过不停更换编码方式实现对于不同编码文件的一起访问
    @Time：2023/7/17 || 20:47 ||20324
    """
    for encoding in encoding_list:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
                return content
        except UnicodeDecodeError:
            continue
    return None


