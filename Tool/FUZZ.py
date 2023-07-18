"""
@FileName：FUZZ.py
@Description:
@Time：2023/7/18 10:53
@user: 20324
"""
import random
import string
class Fuzz:
    def __init__(self,len):
        self.len=len
    # 生成随机字符串
    def generate_random_string(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(self.len))
    # 生成随机整数
    def generate_random_integer(self,min_value, max_value):
        return random.randint(min_value, max_value)
    # 生成随机字节流
    def generate_random_bytes(self):
        return bytes(random.getrandbits(8) for _ in range(self.len))
    def get_result(self):
        random_string = self.generate_random_string()
        random_integer = self.generate_random_integer(1, pow(10,self.len))
        random_bytes = self.generate_random_bytes()
        dict={
            "String": random_string,
            "Integer": random_integer,
            "Bytes": random_bytes
        }
        return dict
        
# 示例用法
obj=Fuzz(10)
dict=obj.get_result()
print("Random String:", dict['String'])
print("Random Integer:", dict["Integer"])
print("Random Bytes:", dict["Bytes"])