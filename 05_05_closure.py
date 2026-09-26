"""
闭包（closure）

一个函数，把它定义时所在外层函数中的变量“记住了”；
即使外层函数已经执行结束，它以后仍然可以使用这些变量

闭包 = 函数 + 它引用的自由变量所对应的环境

"""


"""
闭包的典型结构

    外层函数
    │
    ├── 定义变量 x
    │
    ├── 定义内层函数
    │      └── 使用外层变量 x
    │
    └── 返回内层函数

"""


# -------------------------------------------------------------


def outer():
    x = 10

    def inner():
        print(x)

    return inner

func = outer()
func()  # 10，内层函数还记着变量x，x是inner的闭包变量



"""
观察函数的闭包变量:

    func
    │
    ├── 函数代码
    │
    └── __closure__
        │
        └── cell
                │
                └── 10

"""
print(func.__closure__)     # (<cell at 0x000001F99587A440: int object at 0x00007FFA4111CAD8>,)
print(type(func.__closure__))   # <class 'tuple'>

print(func.__closure__[0])
print(type(func.__closure__[0]))    # <class 'cell'>，cell类型可以理解成：一个专门用来装闭包变量的“小盒子”
print(func.__closure__[0].cell_contents)    # 10


print(func.__code__.co_freevars)    # ('x',)，查看闭包捕获了哪些变量，他不是inner的局部变量，而是来自外层作用域



# -------------------------------------------------------------

"""经典例子"""

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))   # 20
print(triple(10))   # 30


"""关键的区别，注意 multiply 不能写成 multiply() """


# -------------------------------------------------------------


"""闭包：可以 "保存状态" """


def counter():
    count = 0

    def add():
        nonlocal count  #
        count += 1
        return count

    return add

c = counter()

print(c())  # 1
print(c())  # 2
print(c())  # 3

"""
针对上面的代码：如果如果不声明nonlocal，会报错，核心原因为：
    只要 Python 在一个函数体中发现对某个名字有赋值操作，
    它默认就会把这个名字判断为该函数的局部变量，除非你明确使用 global 或 nonlocal

    函数中如果只是读取一个变量，可以按照 LEGB 规则向外寻找；
    但如果对这个名字进行了赋值，Python 默认把它当成当前函数的局部变量。


Python 为什么认为它是 add() 的局部变量？

    因为 Python 在分析 add() 函数的时候看到了：
        count = ...
    也就是赋值。


    于是 Python在编译这个函数时就决定：
        add()
        │
        └── count 是局部变量


    这一步不是等执行到 count += 1 才临时决定的。所以：
        def add():
            count += 1


    大致会遇到这个矛盾：
        Python 分析 add()
                ↓
        发现 count 有赋值操作
                ↓
        因此 count 是 add() 的局部变量
                ↓
        真正执行：
        count += 1
        相当于：
        count = count + 1
                ↑
                先读取 count
                ↓
        但 add() 的局部 count
        还没有被赋过初始值！
                ↓
        UnboundLocalError


"""


# -------------------------------------------------------------

"""
nonlocal是理解闭包的一个关键字

outer() 只执行了一次；执行结束后，x 没有消失，而是被返回的 inner 函数通过闭包保存了下来


注意：
    inner() 用到了 outer() 里面的 x。

所以 Python 发现：
    inner 以后还需要访问 x

因此不能让 outer() 执行结束后直接把 x 丢掉。
Python 会把这个 x 放进一个特殊的 cell 对象 里。
可以想象成：
    outer 执行期间

    x
    ↓
    ┌────────────┐
    │ cell       │
    │ x = 10     │
    └────────────┘
        ↑
        │
    inner

更准确一点：
    func
    │
    ▼
    inner 函数对象
    │
    └── closure
        │
        ▼
        ┌──────────┐
        │ cell     │
        │ x = 10   │
        └──────────┘

因此：outer() 已经执行完
但是：func → inner → cell → x 引用关系仍存在
所以：所以 Python 不能把 x 回收掉，这就是为什么 x 可以一直活着

"""

def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1
        return x

    return inner

func = outer()
print(func.__closure__[0].cell_contents)    # 10

print(func())   # 11，把闭包里保存的那个 x 更新成 11
print(func.__closure__[0].cell_contents)    # 11

print(func())   # 12，没有再执行outer()，闭包里面已经是 x = 11
print(func.__closure__[0].cell_contents)    # 12

print(func())   # 13
print(func.__closure__[0].cell_contents)    # 13

# =============================================================

"""
视频中观察闭包变量的例子
"""

def outer3(m):
    print("outer()函数中的值：", m)

    def inner3(n):
        print("inner()函数中的值：", n)
        return m + n

    return inner3

func3 = outer3(10)
print(func3(20))    # 30
print(func3(60))    # 70

# =============================================================

"""针对作用域非常好的对比"""

"""
1、只读取，自动找外层，没赋值，所以：
    inner 没有局部 x
            ↓
    向外寻找
            ↓
    outer.x = 10
"""

def outer1():
    x = 10

    def inner1():
        print(x)


"""2、直接赋值——创建自己的局部变量"""

def outer2():
    x = 10

    def inner2():
        x = 20
        print(x)


"""
3、既想读取又想修改外层变量——nonlocal，明确告诉python
    不要创建 inner.x
            ↓
    使用 outer.x
            ↓
    读取 10
            ↓
    + 1
            ↓
    重新写回 outer.x
            ↓
    11
"""

def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1