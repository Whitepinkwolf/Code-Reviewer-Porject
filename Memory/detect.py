import clang.cindex

def find_memory_leaks(file_path):
    # 创建Clang索引
    index = clang.cindex.Index.create()

    # 解析C语言文件
    translation_unit = index.parse(file_path)

    # 获取语法树的根节点
    root = translation_unit.cursor

    # 存储内存分配的节点和对应的释放节点
    allocation_nodes = {}

    # 遍历语法树，查找内存分配和释放的匹配对
    for node in root.walk_preorder():
        if node.kind == clang.cindex.CursorKind.CALL_EXPR:
            # 检查内存分配函数
            if node.spelling in ['malloc', 'calloc', 'realloc']:
                # 获取内存分配函数的行号和大小参数
                line = node.location.line
                size = get_memory_allocation_size(node)

                # 存储内存分配节点
                allocation_nodes[line] = {
                    'node': node,
                    'size': size,
                    'freed': False
                }

            # 检查内存释放函数
            elif node.spelling == 'free':
                # 获取内存释放函数的行号和参数
                line = node.location.line
                argument = get_free_argument(node)

                # 查找对应的内存分配节点
                allocation_node = find_matching_allocation(line, argument, allocation_nodes)

                if allocation_node is not None:
                    # 标记该内存分配节点已被释放
                    allocation_node['freed'] = True
                else:
                    print(f"Possible memory leak at line {line}")

    # 输出未释放的内存分配
    for line, allocation_node in allocation_nodes.items():
        if not allocation_node['freed']:
            print(f"Unfreed memory allocation at line {line}")

    print('allocation_nodes: ')
    print(allocation_nodes)

def get_memory_allocation_size(node):
    # 获取内存分配函数的大小参数
    for argument in node.get_arguments():
        if argument.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
            return int(argument.spelling)

    return None

def get_free_argument(node):
    # 获取内存释放函数的参数
    arguments = list(node.get_arguments())
    if arguments:
        return arguments[0].spelling

    return None

def find_matching_allocation(line, argument, allocation_nodes):
    # 在已有的内存分配节点中查找匹配的节点
    for allocation_node in allocation_nodes.values():
        if not allocation_node['freed'] and allocation_node['size'] == argument:
            return allocation_node

    return None

# 指定C语言文件路径
c_file_path = '../test.c'

# 调用函数进行内存泄漏检测
find_memory_leaks(c_file_path)

