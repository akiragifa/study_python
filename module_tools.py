"""
import后，顶层代码会执行。
顶层不是指文件上半部分，而是指：不在函数、类等代码块内部的代码


对于下面的代码，流程为：

    print("Hi")        → 执行，所以打印 Hi

    x = 10             → 执行，创建变量 x

    print(x)           → 执行，所以打印 10

    def greet(...):    → 执行 def，创建 greet 函数对象
                        但不会执行 greet 函数体

    print("下层")      → 执行，所以打印 下层

    def add(...):      → 执行 def，创建 add 函数对象
                        但不会执行 add 函数体

"""

print("Hi")
x = 10
print(x)


def greet(name):
    return f"Hello, {name}"

print("下层")   # 导入时这行代码也会执行


def add(a, b):
    return a + b