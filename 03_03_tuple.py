"""
元组：不可更改，只支持查询操作，不支持增、删、改

应用于：
1、函数的参数和返回值
2、格式化输出后面的()本质上就是元组
3、数据不可以被修改时，保护数据安全

"""

tua = (1, 2, 3)
print(tua)      # (1, 2, 3)
print(type(tua))    # <class 'tuple'>


tua2 = ("akiragifa", 2)
print(tua2)     # ('akiragifa', 2)


tua3 = (1)  # 错误写法，只有1个元素时，后面要加 ","
print(tua3)     # 1
print(type(tua3))   # <class 'int'>


tua4 = (1, )
print(tua4)     # (1,)
print(type(tua4))   # <class 'tuple'>


tua5 = ()
print(tua5)     # ()，空元组
print(type(tua5))   # <class 'tuple'>


tua6 = ("akiragifa", 2)
# tua6[0] = 3     # 报错


tua7 = ("akiragifa", 2, 2, 67, "xingxing")
print(tua7[0])  # akiragifa

print(tua7.count(2))    # 2
print(tua7.index("akiragifa"))  # 0
print(len(tua7))    # 5

tua7[1: ]   # 切片操作不改变原元组
print(tua7)

print(tua7[1: ])    # (2, 2, 67, 'xingxing')
print(type(tua7[1: ]))  # <class 'tuple'>


# -------------------------------------------------------------

"""
格式化输出
"""

name = "akiragifa"
age = 20

info = (name, age)

print("我的名字是%s，今年%d岁" % info)  # 我的名字是akiragifa，今年20岁