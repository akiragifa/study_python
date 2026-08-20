"""
    input() 是 Python 中用来接收用户键盘输入的函数，回车完成输入

    input得到的内容始终是str
"""

name = input("请输入你的名字：")
print("你好，" + name)

age = input("请输入年龄：")
height = int(input("请输入身高："))     # 输入的数字强制转为整数
print(age)
print(type(age))

print(height)
print(type(height))

