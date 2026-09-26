"""
| 函数        | 转换目标 |
| --------- | ---- |
| `int()`   | 整数   |
| `float()` | 浮点数  |
| `str()`   | 字符串  |
| `bool()`  | 布尔值  |
| `list()`  | 列表   |
| `tuple()` | 元组   |
| `set()`   | 集合   |
| `dict()`  | 字典   |


                int
              ↗     ↘
            str     float
              ↘     ↗
                bool


 iterable
   │
   ├────→ list
   │
   ├────→ tuple
   │
   └────→ set


"""

# -------------------------------------------------------------

a = 3.14
int(a)
b = int(a)

print(a)    # 3.14，不会改变原变量，而返回一个新变量
print(b)    # 3


# -------------------------------------------------------------

"""
eval：把字符串当作 Python 表达式执行，并返回表达式的结果

eval() 本质上不是类型转换函数，而是 “表达式求值函数”



字符串
↓
eval()
↓
按照 Python 表达式解释
↓
得到真正的 Python 对象/计算结果



| 函数              | 含义                       |
| --------------- | ------------------------ |
| `int("123")`    | 把 `"123"` 转换为整数          |
| `eval("123")`   | 把 `"123"` 当 Python 表达式求值 |
| `eval("1 + 2")` | 执行表达式 `1 + 2`            |


| 写法                          | 作用              |
| --------------------------- | --------------- |
| `int("123")`                | 类型转换            |
| `eval("1 + 2")`             | 执行 Python 表达式   |
| `ast.literal_eval("[1,2]")` | 安全解析 Python 字面量 |




比 eval() 更安全的方式是：

import ast
data = ast.literal_eval(data)

ast.literal_eval() 只允许解析比较安全的 Python 字面量


"""

result = eval("1 + 2")
print(result)   # 3
print(type(result))     # <class 'int'>



list1 = eval("[1, 2, 3]")
print(list1)    # [1, 2, 3]
print(type(list1))  # <class 'list'>


str1 = eval("'akira'")  # 注意这里有两层引号，外层引号表示整个参数是字符串，内层引号则是 Python 字符串表达式
print(str1)     # akira
print(type(str1))   # <class 'str'>


print(eval("len([1, 2, 3])"))   # 3，函数调用也是表达式

# print(eval("a = 10"))   # 报错，赋值语句不是表达式，能计算出一个值的东西，就是表达式


# -------------------------------------------------------------

""" str -> list """
print(list("abcdefg"), type(list("abcdefg")))   # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] <class 'list'>


""" tuple -> list """
print(list((1, 2, 3)), type(list((1, 2, 3))))   # [1, 2, 3] <class 'list'>


""" dict -> list """
dic3 = {'name': 'akira', 'age': 18}
print(list(dic3), type(list(dic3)))     # ['name', 'age'] <class 'list'>，只会转keys


""" set -> list  可用来去重 """
print(list({1, 3, 3, 4}), type(list({1, 3, 3, 4})))     # [1, 3, 4] <class 'list'>


# -------------------------------------------------------------

dic1 = dict([("name", "akira"), ("age", 18)])
print(dic1)     # {'name': 'akira', 'age': 18}

dic2 = dict(name = "akira", age = 18)
print(dic2)     # {'name': 'akira', 'age': 18}