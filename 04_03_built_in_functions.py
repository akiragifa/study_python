"""
Python
├── 语法
│   ├── if
│   ├── for
│   ├── while
│   ├── def
│   ├── class
│   └── del
│
├── 内置类型
│   ├── int
│   ├── float
│   ├── str
│   ├── list
│   ├── tuple
│   ├── dict
│   ├── set
│   └── bool
│
├── 内置函数
│   ├── print()
│   ├── len()
│   ├── type()
│   ├── id()
│   ├── max()
│   ├── min()
│   ├── sum()
│   ├── sorted()
│   ├── map()
│   ├── filter()
│   └── ...
│
├── 标准库
│   ├── pathlib
│   ├── math
│   ├── os
│   ├── json
│   └── ...
│
└── 第三方库
    ├── numpy
    ├── pandas
    └── ...

"""



import builtins
from os import scandir
import re
from sys import set_coroutine_origin_tracking_depth

"""
    dir(): 查看一个对象拥有哪些属性和方法
    
    大写字母开头一般是内置常量名
    小写字母开头一般是内置函数名
"""
print(dir(builtins))

print(builtins.print)   # <built-in function print>


# -------------------------------------------------------------


"""
    enumerate(): 遍历一个可迭代对象时，自动给每个元素配上一个编号
"""
names = ["xixi", "haha", "akiragifa"]
for index, name in enumerate(names):
    print(index, name)

for item in enumerate(names):
    print(item)
    print(type(item))   # <class 'tuple'>


"""
    type()
"""
print(type(int))    # <class 'type'>


# -------------------------------------------------------------

print(abs(-1))  # 1，返回绝对值
print(sum([1, 2, 3, 4]))    # 10，参数为可迭代对象，求和
# print(sum(1, 4, 5))     # 报错

scores = [80, 50, 70, 40, 90]
count = sum(score >= 60 for score in scores)    # 生成器表达式，True和False也可以sum
print(count)    # 3，返回score >= 60的个数


list1 = [score >= 60 for score in scores]   # 列表推导式
print(list1)    # [True, False, True, False, True]
print(sum(list1))   # 3

# --------------------------

print(min((1, 2, 3, 4)))    # 1，可传入可迭代对象，也可传入多个参数，此处传入的为可迭代对象
print(max([1, 2, 3, 4]))    # 4


print(min(-8, 5))   # -8，此处传入的是多个参数
print(min(-8, 5, key = abs))   # 5


# --------------------------

"""
zip(): 按相同位置，从多个可迭代对象各取一个元素，组成元组

    例子：
                names:  Tom     Jack    Lucy
                ↓       ↓       ↓
        ages:    18      20      19
                ↓       ↓       ↓
        结果:  (Tom,18) (Jack,20) (Lucy,19)

"""

list2 = [1, 2, 3]
list3 = ["a", "b", "c", "d"]

print(zip(list2, list3))    # <zip object at 0x000001C355423340>
print(type(zip(list2, list3)))  # <class 'zip'>
print(list(zip(list2, list3)))  # [(1, 'a'), (2, 'b'), (3, 'c')]

for item in zip(list2, list3):
        print(item)     # (1, 'a') \n (2, 'b') \n (3, 'c')
        print(type(item))   # <class 'tuple'>


# --------------------------

"""map()"""
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))     # [2, 4, 6, 8]


# -------------------------------------------------------------


"""
总结：


                    Python 内置函数
                           │
       ┌───────────────────┼───────────────────┐
       ↓                   ↓                   ↓
    基础操作             数据处理             对象检查
       │                   │                   │
   print()              len()               type()
   input()              max()               isinstance()
                        min()               id()
                        sum()               hash()
                        sorted()            callable()
                           │
                           ↓
                       可迭代对象
                           │
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
     range()           enumerate()          zip()
        │
        ↓
      for循环
                           │
              ┌────────────┴────────────┐
              ↓                         ↓
            map()                    filter()
              │                         │
           转换元素                   筛选元素
              │                         │
              └───────────┬─────────────┘
                          ↓
                       lambda

"""