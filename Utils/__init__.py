import os

header_file_str = 'Header file'
macro_definitions_str = 'Macro definition'

def check_extension(item_path):
    file_extension = os.path.splitext(item_path)[1]
    if file_extension == '.c' or file_extension == '.h':
        return True
    else:
        return False