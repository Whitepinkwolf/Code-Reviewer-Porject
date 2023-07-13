"""
@FileName：crawler.py
@Description:
@Time：2023/7/11 13:50
@user: 20324
"""
import os
import clang.cindex
import re
class Function:
    def __init__(self, name, parameters,return_type,is_definition,line):
        self.name = name
        self.parameters = parameters
        self.return_type=return_type
        self.local_variables = []
        self.is_define=is_definition #声明还是定义
        self.line=line

    def combine_function(self):
        name = self.name
        param_type = [t[0] for t in self.parameters]
        combined = name + "(" + ", ".join(param_type) + ")"
        return combined
class Variable:
    def __init__(self, name, type,line):
        self.name = name
        self.type = type
        self.line=line
class Macro:
    def __init__(self,name,content,line):
        # #define a 10   ,name=a  content=10
        self.name=name
        self.value=content
        self.line=line
class Include:
    def __init__(self,name,line):
        self.name=name
        self.line=line

class Struct:
    def __init__(self, name, fields,line):
        self.name = name
        self.fields = fields
        self.line=line


class File:
    def __init__(self,filepath):
        self.fun_list=[]
        self.var_list = []
        self.macro_list=[]
        self.struct_list=[]
        self.include_list=[]
        self.file_path=filepath.replace("/", "\\")
    def find_define(self):
        #  define：匹配 #define 字符串。
        # \s +：匹配一个或多个空白字符。
        # (\w+)：匹配一个或多个字母数字字符（宏名称）。
        # (\d+)：匹配一个或多个数字字符（宏值）。
        macro_pattern = r'#define\s+(\w+)\s+(\w+)'
        # ^ ：表示匹配字符串的开头。
        # \s *：表示匹配零个或多个空白字符（包括空格、制表符、换行符等）。
        # # include：表示匹配字面字符串 "#include"。
        # \s +：表示匹配一个或多个空白字符。
        # "：表示匹配一个双引号。
        # ([ ^ "]+)：表示一个捕获组，用于匹配一个或多个非双引号字符。
        #      "：表示匹配一个双引号。
        pattern1 = r'^\s*#include\s*<([^>]+)>'
        pattern2 = r'^\s*#include\s*"([^"]+)"'
        with open(self.file_path,'r', encoding='utf-8') as file:
            lines = file.readlines()
            index = 1
            # print(lines)
            for line in lines:
                if line.startswith('#include'):
                    matche1 = re.findall(pattern1, line)
                    matche2 = re.findall(pattern2, line)
                    if matche1:
                        self.include_list.append(Include(matche1, index))
                    else:
                        self.include_list.append(Include(matche2, index))
                elif line.startswith('#define'):
                    matches = re.findall(macro_pattern, line)
                    if matches:
                        for match in matches:
                            macro_name = match[0]
                            macro_value = match[1]
                            self.macro_list.append(Macro(macro_name, macro_value, index))
                index = index + 1
        file.close()



    def parse_functions(self, translation_unit):
        current_file_path = os.path.abspath(self.file_path)
        for node in translation_unit.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                function_location = node.extent.start.file.name

                if function_location == current_file_path:
                    function_name = node.spelling
                    function_line = node.extent.start.line
                    parameters = []
                    return_type = node.result_type.spelling
                    is_definition = False
                    for child_node in node.get_children():
                        if child_node.kind == clang.cindex.CursorKind.COMPOUND_STMT:
                            is_definition = True
                    for child_node in node.get_children():
                        if child_node.kind == clang.cindex.CursorKind.PARM_DECL:
                            parameter_type = child_node.type.spelling
                            parameter_name = child_node.spelling

                            parameters.append((parameter_type, parameter_name))
                    function = Function(function_name, parameters, return_type, is_definition,function_line)
                    self.fun_list.append(function)

    def parse_global_variables(self, translation_unit):
        current_file_path = os.path.abspath(self.file_path)

        for node in translation_unit.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.VAR_DECL and \
                    node.semantic_parent.kind == clang.cindex.CursorKind.TRANSLATION_UNIT:
                variable_location = node.extent.start.file.name

                if variable_location == current_file_path:
                    variable_name = node.spelling
                    variable_type = node.type.spelling
                    variable_line = node.extent.start.line
                    variable = Variable(variable_name, variable_type,variable_line)
                    self.var_list.append(variable)

    def parse_structs(self, translation_unit):
        current_file_path = os.path.abspath(self.file_path)

        for node in translation_unit.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.STRUCT_DECL:
                struct_location = node.extent.start.file.name

                if struct_location == current_file_path:
                    struct_name = node.spelling
                    fields = [(f.spelling, f.type.spelling) for f in node.get_children() if
                              f.kind == clang.cindex.CursorKind.FIELD_DECL]
                    struct_line=node.extent.start.line
                    struct = Struct(struct_name, fields,struct_line)
                    self.struct_list.append(struct)

    def parse_local_variables(self, translation_unit):
        for node in translation_unit.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.VAR_DECL and \
                    node.semantic_parent.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                variable_name = node.spelling
                variable_type = node.type.spelling
                variable_line = node.extent.start.line  # 获取变量声明语句的行号
                parent_function_name = node.semantic_parent.spelling
                for function in self.fun_list:
                    if function.name == parent_function_name:
                        variable = Variable(variable_name, variable_type,variable_line)
                        function.local_variables.append(variable)

    def get_translation(self):
        file_path = self.file_path
        index = clang.cindex.Index.create()
        translation_unit = index.parse(file_path)
        return translation_unit

    def parse_c_file(self):
        self.find_define()

        translation_unit = self.get_translation()

        self.parse_functions(translation_unit)
        self.parse_global_variables(translation_unit)
        self.parse_local_variables(translation_unit)
        self.parse_structs(translation_unit)

        return self.fun_list, self.macro_list, self.struct_list, self.var_list

    def get_function_name(self):
        """
        @description: 仅仅获取文件名字,注意encoding方式
        @Time：2023/7/13 || 16:18 ||20324
        """
        translation_unit = self.get_translation()
        fun_list = []
        with open(self.file_path, 'r',encoding='utf-8') as file:
            content = file.read()
        for node in translation_unit.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                function_location = node.extent.start.file.name
                function_name = node.spelling
                if function_exists_in_file(content,function_name):
                    fun_list.append(function_name)
        file.close()
        return fun_list

def function_exists_in_file(content,function_name):
    pattern = r'\b' + re.escape(function_name) + r'\b'
    match = re.search(pattern, content)
    if match:        return True
    else:        return False

# 测试示例
if __name__ == "__main__":
    file_path = "D:\\project_code\\pythonproject\\CodeAuditing\\test_c\\graph.c"
    file_obj=File(file_path)
    print(file_obj.get_function_name())
    # file_obj.parse_c_file()
    # for function in file_obj.fun_list:
    #     print(f"___________Function:{function.name}  {function.line}")
    #     print("Parameters:", function.parameters)
    #     print("return:",function.return_type)
    #     print("is defined?:",function.is_define)
    #     print("Local Variables:")
    #     for variable in function.local_variables:
    #         print(f"{variable.type} {variable.name} {variable.line}")
    # for macro in file_obj.macro_list:
    #     print(f"___________Macro:{macro.name},value:{macro.value},line {macro.line}", )
    # for include in file_obj.include_list:
    #     print(f"___________include_list:{include.name}.line{include.line}")
    # for struct in file_obj.struct_list:
    #     print(f"___________Struct:{struct.name}")
    #     print("Fields:")
    #     for field in struct.fields:
    #         print(field[0], ":", field[1])
    # for variable in file_obj.var_list:
    #     print('___________Gobal var:')
    #     print(variable.name, ":", variable.type)