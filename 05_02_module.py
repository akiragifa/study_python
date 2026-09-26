"""
一个 .py 文件，就是一个 Python 模块

分类：
    内置模块：random、time、os等
    第三方模块（第三方库）：通过pip安装的模块都是第三方模块
    自己写的模块

一个模块里可包含：
    模块
    │
    ├─ 变量
    ├─ 函数
    ├─ 类
    ├─ 常量
    └─ 其他 Python 代码

==============================

形式：

import module

调用时: module.xxx

------------------------------

from module import xxx

xxx直接使用，不用写 module.xxx

------------------------------

import numpy as np

给模块起别名

------------------------------

from pathlib import Path as P

给函数起别名

------------------------------

from math import *

表示把 math 模块中的很多公开名字直接导入当前命名空间

于是可以直接 sqrt(16), sin(1), cos(1)，不需要 math.sqrt(), 但是不推荐

==============================

"""

# -------------------------------------------------------------


"""
概念区分：

模块：通常就是一个 .py 文件，例：
    math_tools.py

包：通常包含多个模块的目录，例：
    mypackage/
    │
    ├─ __init__.py  包会包含这个文件
    ├─ math_tools.py
    └─ file_tools.py

库：更宽泛的概念，一个库可能包含：
    很多包
    很多模块
    很多类
    很多函数

    

可以这样理解：
    库
    │
    └─ 包
    │
    └─ 模块
        │
        ├─ 类
        ├─ 函数
        └─ 变量

"""




"""
模块本身也是对象
"""

import math

print(type(math))   # <class 'module'>

# -------------------------------------------------------------

"""自定义模块"""

# import module_tools

# print(module_tools.greet("Tom"))    # Hello, Tom
# print(module_tools.add(1, 2))   # 3


import module_tools2    # 只打印 "顶层"

print(module_tools2)    # <module 'module_tools2' from 'e:\\study_code\\study_python\\module_tools2.py'>
print(type(module_tools2))  # <class 'module'>

print(module_tools2.__name__)   # module_tools2

from module_tools2 import name
print(name)     # akiragifa，可以通过这种方式导入变量


# -------------------------------------------------------------

"""
Python怎样找到模块

简单理解：
    import tools
    ↓
    Python 去模块搜索路径中寻找 tools
    ↓
    找到 tools.py
    ↓
    加载并执行
    ↓
    创建 module 对象
    ↓
    名字 tools 指向这个对象

"""

import sys
print(sys.path)     # 表示 Python 在执行 import xxx 时，会去哪些目录寻找 xxx

"""
上面代码的运行结果：

['e:\\study_code\\study_python',
'D:\\Program_tools\\Python313\\python313.zip',
'D:\\Program_tools\\Python313\\DLLs',
'D:\\Program_tools\\Python313\\Lib',
'D:\\Program_tools\\Python313',
'D:\\Program_tools\\Python313\\Lib\\site-packages',
'E:\\study_code\\skill_playground_mattpocock_skills\\src']


分类：
    sys.path
    │
    ├─ e:\study_code\study_python
    │   └─ 当前运行脚本所在目录
    │
    ├─ D:\Program_tools\Python313\python313.zip
    ├─ D:\Program_tools\Python313\DLLs
    ├─ D:\Program_tools\Python313\Lib
    ├─ D:\Program_tools\Python313
    │   └─ Python 自身相关路径
    │
    ├─ D:\Program_tools\Python313\Lib\site-packages
    │   └─ 第三方库安装目录
    │
    └─ E:\study_code\skill_playground_mattpocock_skills\src
        └─ 额外被加入的搜索路径，说明我的 Python 环境中，某个配置把这个 src 目录额外加入了 sys.path，查看 “D:\Program_tools\Python313\Lib\site-packages” 路径下的 *.pth 文件就可看到，这个E盘的路径被加入进去了，整个过程可能是：
            启动 Python
                ↓
            加载 site 模块
                ↓
            检查 site-packages
                ↓
            发现 .pth / editable install 配置
                ↓
            发现：
            E:\study_code\skill_playground_mattpocock_skills\src
                ↓
            加入 sys.path

"""

import site

print(site.getsitepackages())