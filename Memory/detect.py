from Memory.tool_Clang import ToolClang ,get_available_llvm_path
from Memory.tool_memory import ToolMemoryChecker
from Memory.tool_cppchecker import ToolCppChecker
from Memory.tool_flawfinder import ToolFlawfinder
from Utils import llvm_path

def memory_merge(file_path):
    result=[]
    #cppcheck 工具
    cppcheck_obj=ToolCppChecker(file_path)
    cppcheck_obj.run_scan()
    cpp_return={'cppcheckertext':cppcheck_obj.output}
    result.append(cpp_return)
    #drmemory内存检测工具
    drmemory_obj=ToolMemoryChecker(file_path)
    errors,errors_summery=drmemory_obj.extract_memory_leaks()
    drmemory_text={'drmemory_error':errors,
                   'drmemory_summery':errors_summery}
    result.append(drmemory_text)

    #clang 包括 clangcheck and clangvauation
    llvm_path0 = get_available_llvm_path(llvm_path) #获取正确的llvm（我们多个人写了多个路径，会自动寻找合适的path）
    clang_obj=ToolClang(file_path,llvm_path0)
    clang_obj.format_code()
    clang_obj.run_static_scan_strict()
    clang_obj.run_compile()
    clang_obj.run_static_scan()
    clang_obj.run_exec()
    clang_obj.run_static_scan_report()
    clang_obj.run_code_quality_evaluation()

    clang_check_return={'clangcheckertext':clang_obj.static_scan_strict_error}
    result.append(clang_check_return)

    clang_valuation_return={'clangevaluationtext': clang_obj.code_evaluation_error}
    result.append(clang_valuation_return)

    tool_flawfinder = ToolFlawfinder(file_path)
    tool_flawfinder.run()
    tool_flawfinder.get_data()
    tool_flawfinder.get_graph_base_data()
    tool_flawfinder_dict={'Flawfindertext': tool_flawfinder.result_text,
          'copy_right': tool_flawfinder.copy_right,
          'detect_rules': tool_flawfinder.detect_rules,
          'examing_file': tool_flawfinder.examing_file,
          'final_results': tool_flawfinder.final_results,
          'analysis_summary': tool_flawfinder.analysis_summary,
          'hits': tool_flawfinder.hits,
          'detect_lines': tool_flawfinder.detect_lines,
          'detect_real_lines': tool_flawfinder.detect_real_lines,
          'Minimum_risk_level': tool_flawfinder.Minimum_risk_level,
          'levels': tool_flawfinder.levels,
          'levels_plus': tool_flawfinder.levels_plus,
          'levels_plus_KSLOC': tool_flawfinder.levels_plus_KSLOC
          }
    result.append(tool_flawfinder_dict)
    return result
if __name__=='__main__':
    file_path = r'D:\project_code\pythonproject\CodeAuditing\test_c\test.c'
    result=memory_merge(file_path)
    for dict in result:
        for key,value in dict.items():
            print(key,":",value)



