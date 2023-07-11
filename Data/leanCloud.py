# 参考 https://leancloud.cn/docs/sdk_setup-python.html, https://leancloud.github.io/python-sdk/

import leancloud

appId = 'hrwjWdJzRfN5ewluWwtvoono-gzGzoHsz'
appKey = 'J4WDUUz6lekpuSAGiVpLvF3x'
masterkey = "ZDm5SkP4WOnkeK7suMar3gmU"

'''初始化'''
# lean_initialization = leancloud.init(appId, appKey)
lean_initialization = leancloud.init(appId, master_key=masterkey)
#print(lean_initialization)  #None

'''开启调试日志'''
# 调试日志开启后，SDK 会把网络请求、错误消息等信息输出到 IDE 的日志窗口，
# 或是浏览器 Console 或是云引擎日志（如果在云引擎下运行 SDK）。
# import logging
# logging.basicConfig(level=logging.DEBUG)

# '''验证'''
# TestObject = leancloud.Object.extend('TestObject')  #派生一个新的 leancloud.Object 子类 TestObject
# test_object = TestObject()
# test_object.set('words', "Hello world!")    #在当前对象此字段(words)上赋值(Hello world!)
# test_object.save()   #将对象数据保存至服务器

# '''风险函数存储'''
# RiskFunctionObject = leancloud.Object.extend('RiskFunctionObject')
# riskFunctionObject = RiskFunctionObject()
# riskFunctionObject.set('FunctionName', "gets")
# riskFunctionObject.set('RiskLevel', "最危险")
# riskFunctionObject.set('Solution', "使用更安全的fgets()函数或定义足够大的数组空间")
# riskFunctionObject.save()

'''风险函数打印'''
def riskFunctionShow(riskFunction):
    print(f'objectId = {riskFunction.get("objectId")}, '
          f'FunctionName = {riskFunction.get("FunctionName")}, '
          f'RiskLevel = {riskFunction.get("RiskLevel")}, '
          f'Solution = {riskFunction.get("Solution")}, ')

'''风险函数查询'''
def riskFunctionQuery():
    '''
    基础查询: 创建Object.query查询对象，用equal_to设置查询条件，用find进行查询
        构建 leancloud.Query；
        向其添加查询条件；
        执行查询并获取包含满足条件的对象的数组。
    '''
    RiskFunctionObject = leancloud.Object.extend('RiskFunctionObject')
    query = RiskFunctionObject.query
    # 以上两行等价于 query = leancloud.Query('Student')
    query.equal_to('FunctionName', 'vsnprintf')
    RiskFunction_list = query.find()
    for riskFunction in RiskFunction_list:
        riskFunctionShow(riskFunction)

'''用户信息存储'''
def UserStore(username, password):
    UserObject = leancloud.Object.extend('UserObject')
    userObject = UserObject()
    userObject.set('Username', username)
    userObject.set('Password', password)
    userObject.save()

'''用户信息打印'''
def UserShow(riskFunction):
    print(f'objectId = {riskFunction.get("objectId")}, '
          f'Username = {riskFunction.get("username")}, '
          f'Password = {riskFunction.get("password")}, ')

'''用户信息匹配'''
def UserQuery(Login_username):
    '''
    基础查询: 创建Object.query查询对象，用equal_to设置查询条件，用find进行查询
        构建 leancloud.Query；
        向其添加查询条件；
        执行查询并获取包含满足条件的对象的数组。
    '''
    query = leancloud.Query('UserObject')
    query.equal_to('Username', Login_username)
    User_list = query.find()
    for User in User_list:
        return User.get("Password")



