"""
@FileName：database.py
@Description:数据库操作接口
@Time：2023/7/6 14:31
@user: 20324
"""
import pymysql

def main():

    db=DataBase()
    db.login('root','AS132619','localhost')
    db_name='code3'
    table_name='third_table'
    keys={'id':'int',
          'name':'text'}
    primary_key_name='id'
    print_list=[]
    data=[
        (2,'liuqi2'),
        (3,'hahh')
    ]
    # db.delete_database('code2')
    # db.delete_table(db_name,table_name)

    # db.create_database(db_name)
    # db.create_table(db_name,table_name,keys,primary_key_name)

    # print_list=db.query_table(db_name)
    # print_list=db.query_database()
    db.insert_data(data,db_name,table_name)
    print_list = db.query_keys(db_name,table_name)
    print(print_list)

class DataBase:
    def __init__(self):
        self.conn = None
        self.is_logged_in = False

    def login(self,user,password,host):
        try:
            self.conn = pymysql.connect(
                host=host,
                user=user,
                password=password
            )
            self.is_logged_in=True
        except pymysql.Error as e:
            exit("无法连接到数据库:{e}".format(e=e))

    def close(self):
        self.conn.close()

    def create_database(self,database_name):
        query=f"SHOW DATABASES LIKE '{database_name}'"
        if len(self.runSql(query))==0:
            sql = f"CREATE DATABASE {database_name}"
            self.runSql(sql)
        else:
            exit(f'create error:the {database_name} is existed')

    def create_table(self,db_name,table_name,keys,primary_key_name):
        """
        @description: 创建指定的表
        keys为字典类型，表的键
        primary_key_name:首键的name，如果在keys存在就会创建主键
        @Time：2023/7/10 || 11:45 ||20324
        """
        query = f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{db_name}' AND table_name = '{table_name}'"
        if len(self.runSql(query)) == 0:
            columns = []  # 获取键值对
            for key, value in keys.items():
                columns.append(f"{key} {value}")
            primary_key = ""
            if primary_key_name in keys.keys():
                primary_key = f", PRIMARY KEY ({primary_key_name})"
            sql = f'''CREATE TABLE {db_name}.{table_name}(
                                                           {", ".join(columns)}
                                                           {primary_key}
                                                           ) '''
            self.runSql(sql)
        else:
            exit(f'create error:the {db_name}.{table_name} is existed')

    def delete_database(self,database_name):
        query=f"SHOW DATABASES LIKE '{database_name}'"
        result= self.runSql(query)
        if len(result)!=0:
            sql = f"DROP database {database_name}"
            self.runSql(sql)
        else:
            exit(f'delete error:the {database_name} is not exists')

    def delete_table(self,database_name,table_name):
        query=f'''  SELECT table_name FROM information_schema.tables 
        WHERE table_schema = '{database_name}' AND table_name = '{table_name}'
        '''
        if len(self.runSql(query)):
            sql = f"DROP table {database_name}.{table_name}"
            self.runSql(sql)
        else:
            exit(f'delete error:the {database_name}.{table_name} is not exists')

    def runSql(self,command):
        """
        @description: result是一个列表，其中包含了查询结果的所有行数据。每个行数据以元组的形式存储在列表中。
        @Time：2023/7/10 || 8:52 ||20324
        """
        if not self.is_logged_in:
            exit('数据库未登录')
        cur = self.conn.cursor()
        result=()
        try:
            cur.execute(command)
            result = cur.fetchall()  #获取数据
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            exit(f'运行SQL错误，command={command}')
        cur.close()
        return result

    def query_table(self,database):
        sql="SHOW TABLES FROM {}".format(database)
        result = self.runSql(sql)
        table_names = [row[0] for row in result]
        return table_names

    def query_keys(self,database,table):
        sql = f"DESCRIBE {database}.{table}"
        result = self.runSql(sql)
        keys = [row[0] for row in result]
        return keys

    def query_database(self):
        sql='SHOW DATABASES'
        result = self.runSql(sql)
        dbs = [row[0] for row in result]
        return dbs

    def insert_data(self, data, database, table):
        """
        @description:
        接受list存储的 dict 或者 tuple
        @Time：2023/7/10 || 11:42 ||20324
        """
        if not self.is_logged_in:
            exit('数据库未登录')
        cur = self.conn.cursor()
        keys = self.query_keys(database, table)  # 获取表的字段列表
        if isinstance(data, list):
            for item in data:
                if isinstance(item, tuple):
                    values = item
                    placeholders = ', '.join(['%s'] * len(keys))  # 传递占位符防止SQL注入攻击
                    sql = f"INSERT INTO {database}.{table} ({', '.join(keys)}) VALUES ({placeholders})"
                    try:
                        cur.execute(sql, values)
                        self.conn.commit()
                    except Exception as e:
                        self.conn.rollback()
                        exit(f'插入数据错误，数据：{item}，错误信息：{str(e)}')

                elif isinstance(item, dict):
                    values=[]
                    for key in keys:
                        value = item.get(key, None)
                        values.append(value)
                    placeholders = ', '.join(['%s'] * len(keys))
                    sql = f"INSERT INTO {database}.{table} ({', '.join(keys)}) VALUES ({placeholders})"
                    try:
                        cur.execute(sql, values)
                        self.conn.commit()
                    except Exception as e:
                        self.conn.rollback()
                        exit(f'插入数据错误，数据：{item}，错误信息：{str(e)}')
                else:
                    exit('输入的数据类型错误，应为 list+tuple')
        else:
            exit('数据类型错误，应为列表类型')

        cur.close()


if __name__=='__main__':
    main()