import clang.cindex

class Getdata:
    def __init__(self, c_file):
        self.c_file = c_file
        self.file_content = ''
        self.header_files = []
        self.macro_definitions = []
        self.variable_names = []
        self.function_declarations = []
        self.variable_names_all = []
        self.function_declarations_all = []

    def get_unique_datas(self, lists):
        unique_lists = list(set(lists))
        return unique_lists;

    def get_file_info_pre(self):
        with open(self.c_file, 'r') as file:
            lines = file.readlines()
            # print(lines)
            for line in lines:
                if line.startswith('#include'):
                    self.header_files.append(line.strip())
                elif line.startswith('#define'):
                    self.macro_definitions.append(line.strip())
                self.file_content += line
        self.header_files = self.get_unique_datas(self.header_files)
        self.macro_definitions = self.get_unique_datas(self.macro_definitions)

        return self.file_content, self.header_files, self.macro_definitions

    def get_local_info(self):
        index = clang.cindex.Index.create()
        tu = index.parse(self.c_file)

        for node in tu.cursor.walk_preorder():
            if node.location.file is not None and node.location.file.name == self.c_file:
                if node.kind == clang.cindex.CursorKind.VAR_DECL:
                    var_name = node.spelling
                    var_type = node.type.spelling
                    self.variable_names.append((var_name, var_type))
                elif node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                    func_name = node.spelling
                    func_type = node.type.spelling
                    self.function_declarations.append((func_name, func_type))

        return self.variable_names, self.function_declarations

    def get_exter_info(self):
        index = clang.cindex.Index.create()
        tu = index.parse(self.c_file)

        for node in tu.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.VAR_DECL:
                var_name = node.spelling
                var_type = node.type.spelling
                self.variable_names_all.append((var_name, var_type))
            elif node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                func_name = node.spelling
                func_type = node.type.spelling
                self.function_declarations_all.append((func_name, func_type))

        return self.variable_names_all, self.function_declarations_all

    def get_all_local_data(self):
        return self.file_content, self.header_files, self.macro_definitions, self.variable_names, self.function_declarations

    def get_all_exter_data(self):
        return self.file_content, self.header_files, self.macro_definitions, self.variable_names_all, self.function_declarations_all

