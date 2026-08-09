"""
严格来说：
Python 中的布尔型（bool）不属于 Python 官方定义的数值类型（Numeric Types），但它在实现上是整数类型 int 的子类。
这是 Python 一个比较特殊的设计。

分类上
Numeric Types
│
├── int
├── float
└── complex


Boolean Type
└── bool

但是bool继承自int，验证 isinstance(True, int)，结果为True
"""

print(type(True))   # <class 'bool'>

print(isinstance(True, int))    # True

# -------------------------------------------------------------

"""
数字上：
True → 1
False → 0
但是不要把 bool 当整数使用
"""

print(True == 1)    # True
print(False == 0)   # True

print(True + True)  # 2
print(True + False)     # 1
print(False + False)    # 0

print(type(True + True))    # <class 'int'>