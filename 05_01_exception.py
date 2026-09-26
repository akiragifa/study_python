"""
异常机制：
    Python 执行代码时，如果遇到无法正常继续的情况，就会抛出一个异常对象；
    如果某个 except 捕获了这个异常，就进行处理，否则异常会沿函数调用链向上传播，
    最终打印 Traceback 并终止程序

==============================

语法汇总：

try:
    ...
except:     基类异常
    ...

------------------------------

try:
    ...
except Exception:       捕获任意异常
    ...

------------------------------

try:
    ...
except NameError as e:      捕获特定异常
    ...

------------------------------

try:
    ...
except:
    ...
else:
    ...     如果try中没有发生异常，就执行这里

------------------------------

try:
    ...
except:     
    ...
finally:
    ...     不管有没有异常，最终都执行

------------------------------

完整结构：

try:
    ...
except SomeError:
    ...
except AnotherError:
    ...
else:
    ...
finally:
    ...


执行逻辑：
                try
                 │
        ┌────────┴────────┐
        │                 │
     有异常             无异常
        │                 │
        ▼                 ▼
     except              else
        │                 │
        └────────┬────────┘
                 ▼
              finally


------------------------------

raise：主动抛出异常

raise ValueError("年龄不能小于0")   # 例子


"""



# a = 10 / 0  # ZeroDivisionError：除数为0
# print(a)


"""
上面的代码报错：

Traceback (most recent call last):
  File "e:\study_code\study_python\05_01_exception.py", line 3, in <module>
    a = 10 / 0
ZeroDivisionError: division by zero

ZeroDivisionError：异常类型
division by zero：异常信息
Traceback：告诉你异常是沿着怎样的调用路径发生的

"""



"""
Python 报错
│
├─ 语法阶段出错
│   └─ SyntaxError
│
└─ 运行过程中出问题
    └─ Exception
        ├─ ZeroDivisionError
        ├─ TypeError
        ├─ ValueError
        ├─ FileNotFoundError
        └─ ...

"""


"""
重要：异常本质上也是对象

可以按照下面的流程理解下面的代码：
    发生除零错误
        ↓
    Python 创建一个 ZeroDivisionError 对象
        ↓
    这个对象携带错误信息
        ↓
    Python 开始寻找有没有代码愿意处理它

    
语法：
try:
    可能发生异常的代码
except 某种异常:
    发生异常后执行的代码
"""

try:
    10 / 0
except ZeroDivisionError as e:
    print(e)    # division by zero
    print(type(e))      # <class 'ZeroDivisionError'>


# "10" + 20   # TypeError


# int("abc")      # ValueError


# li = ["a", "b", "c"]
# print(li[10])   # IndexError


# person = {"name": "akiragifa", "age": 18}
# print(person["school"])     # KeyError


# print(akira)    # NameError


# name = "hello"
# name.append("a")    # AttributeError，str没有append方法


# with open("abc.txt", "r") as file:
    # text = file.read()      # FileNotFoundError


#  print("xixi")  # IndentationError：缩进错误


"""
一次捕获多个异常
"""
try:
    number = int(input("请输入数字："))
    result = 10 / number
    print(result)
except ValueError:
    print("你输入的不是数字")
except ZeroDivisionError:
    print("不能输入0")


"""
Python的异常类型之间存在继承关系，Exception是绝大多数普通程序异常的父类

BaseException
│
├─ SystemExit
├─ KeyboardInterrupt
│
└─ Exception
    │
    ├─ ArithmeticError
    │   └─ ZeroDivisionError
    │
    ├─ ValueError
    │
    ├─ TypeError
    │
    ├─ LookupError
    │   ├─ IndexError
    │   └─ KeyError
    │
    ├─ OSError
    │   ├─ FileNotFoundError
    │   └─ PermissionError
    │
    └─ ...

"""

# -------------------------------------------------------------


"""完整例子"""

from pathlib import Path

file_path = Path("data.txt")

try:
    text = file_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("文件不存在")
except PermissionError:
    print("没有文件读取权限")
else:
    print("文件读取成功")
    print(text)
finally:
    print("文件读取操作结束")


# -------------------------------------------------------------

"""raise：主动抛出异常"""

def set_age(age):
    if age < 0:
        raise ValueError("年龄不能小于0")

    print(age)

set_age(20)


# -------------------------------------------------------------

"""异常的向上传播"""

def func3():
    return 10 / 0

def func2():
    return func3()

def func1():
    return func2()

# func1()

"""
调用过程：
    func1()
    ↓
    func2()
    ↓
    func3()
    ↓
    10 / 0
    ↓
    ZeroDivisionError


func3()没有处理，异常向上传给func2()
func2()没有处理，异常向上传给func1()
func1()也没有处理，最后传给Python顶层
程序终止并打印：Traceback


异常传播过程可以理解为：

    异常发生
    ↓
    当前函数处理了吗？
    │
    ├─ 是 → except 处理
    │
    └─ 否
        ↓
    传给调用它的函数
        ↓
    继续向上找
        ↓
    一直没人处理
        ↓
    程序终止 + Traceback


"""

"""
上面程序的Traceback：

    Traceback (most recent call last):
    File "e:\study_code\study_python\05_01_exception.py", line 251, in <module>
        func1()
        ~~~~~^^
    File "e:\study_code\study_python\05_01_exception.py", line 249, in func1
        return func2()
    File "e:\study_code\study_python\05_01_exception.py", line 246, in func2
        return func3()
    File "e:\study_code\study_python\05_01_exception.py", line 243, in func3
        return 10 / 0
            ~~~^~~
    ZeroDivisionError: division by zero

实际上是在告诉：

    main
    ↓
    func1
    ↓
    func2
    ↓
    func3
    ↓
    真正出错的位置

traceback也要关注下面几行

"""


# -------------------------------------------------------------


"""
把异常理解成“对象 + 传播机制”，以  int("abc") 为例：

    执行 int("abc")
        ↓
    转换失败
        ↓
    创建 ValueError 异常对象
        ↓
    抛出异常
        ↓
    当前代码有没有 except ValueError？
        │
        ├─ 有 → 捕获并处理
        │
        └─ 没有
            ↓
        向上一层调用者传播
            ↓
        一直没人处理
            ↓
        打印 Traceback
            ↓
        程序终止


"""