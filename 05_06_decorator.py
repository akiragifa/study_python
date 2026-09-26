"""
装饰器：在不修改原函数代码的情况下，给原函数增加额外功能

装饰器最大的价值之一：
    把日志、计时、权限检查、缓存等通用功能从业务函数中分离出来

"""

"""
经典结构：下述函数相当于：

    原来：
        hello ──────→ 原 hello 函数


    装饰以后：
        hello ──────→ wrapper 函数
                        │
                        ├── 执行额外代码
                        │
                        ├── 调用原 hello()
                        │
                        └── 执行额外代码

"""
def decorator(func):
    def wrapper():
        print("函数执行前")

        func()

        print("函数执行后")

    return wrapper


# def hello():
#     print("hello")

# hello = decorator(hello)


"""上面三行代码相当于："""
@decorator  # hello = decorator(hello) 的语法糖
def hello():
    print("hello")

hello()     # 函数执行前 \n hello \n 函数执行后，实际执行的时 wrapper()

print(hello.__name__)   # wrapper，需注意，函数名称发生改变


"""
再次针对上面代码的解释：

wrapper()使用了外层函数decorator()中的变量func，所以wrapper形成了闭包，
即使decorator(hello)执行以后，wrapper仍然记得func指向哪个函数，结构是：

    decorator(func)
    │
    ├── func ─────────────→ 原 hello 函数
    │
    ├── 定义 wrapper()
    │       │
    │       └── 使用外层变量 func
    │
    └── return wrapper
            │
            ▼
            闭包

"""


# =============================================================


"""
装饰有参数的函数
"""

def decorator2(func):

    def wrapper2(*args, **kwargs):
        print("开始执行：")
        result = func(*args, **kwargs)  # 将接收到的参数原样交给原函数
        print("执行结束。")
        return result

    return wrapper2


@decorator2
def add(a, b):
    return a + b

result = add(10, 20)
print(result)   # 30


# =============================================================

"""
常见例子：统计运行时间
"""

import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"运行时间：{end - start:.3f} 秒")

        return result

    return wrapper


@timer
def read_d3hsp():
    print("读取d3hsp...")

read_d3hsp()
print(read_d3hsp())     # None


# =============================================================

"""需要注意，装饰后函数名称改变"""

def decorator3(func):
    def wrapper3():
        print("函数执行前")

        func()

        print("函数执行后")

    return wrapper3


@decorator3
def hello():
    print("hello")

hello()

print(hello.__name__)   # wrapper，需注意，函数名称发生改变，这会导致函数名称、文档字符串等元数据丢失


"""因此，工程代码通常使用functools.wraps，标准写法一般是："""

from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("开始")

        result = func(*args, **kwargs)

        print("结束")

        return result

    return wrapper


@decorator
def hello():
    """这是hello函数"""
    print("hello")


hello()
print(hello.__name__)   # hello


# =============================================================

"""
装饰器本身也可以带参数

如：
    @retry(3)
    def download():
        ...

这比普通装饰器又多了一层函数
"""

def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):

            print("函数执行前：---")
            for _ in range(n):

                func(*args, **kwargs)

            print("函数执行后：===")
            

        """
        对于下行代码输出 ('decorator', 'n') 的解释：
            decorator这个名字也不是 decorator() 的局部变量，
            它是在外层 repeat() 中创建并绑定的函数名，
            所以对 decorator() 自己的代码来说，decorator 这个名字也是从外层作用域取得的，
            因此也被列进 co_freevars

        可以把作用域画成：
            repeat() 的作用域
            ┌─────────────────────────────┐
            │ n = 3                       │
            │                             │
            │ decorator ───► 函数对象     │
            │      ▲                      │
            │      │                      │
            │      └──── decorator内部引用│
            └─────────────────────────────┘

        decorator() 内部实际上引用了两个外层名字：n  decorator

        """
        # print(decorator.__code__.co_freevars)   # ('decorator', 'n')

        return wrapper

    print(decorator.__code__.co_freevars)   # ('n',)

    return decorator


@repeat(3)  # 等价于 hello = repeat(3)(hello)
def hello():
    print("hello3")


hello()     # 函数执行前：--- \n hello3 \n hello3 \n hello3 \n 函数执行后：===


print("hello的闭包变量：", hello.__code__.co_freevars)  # ('func', 'n')
print("hello的闭包变量值1：", hello.__closure__[0].cell_contents)   # <function hello at 0x000002AAE91347C0>
print("hello的闭包变量值2：", hello.__closure__[1].cell_contents)   # 3



"""
上述函数可简化理解为：
    Global
    │
    ├── repeat ───────────────► repeat函数
    │
    └── hello ────────────────► wrapper函数
                                │
                                ├── closure: n ─────► 3
                                │
                                └── closure: func ──► 原始hello函数

然后：
    hello()
    │
    ▼
    wrapper()
    │
    ├── print 函数执行前
    │
    ├── func() ──► 原始hello() ──► hello3
    ├── func() ──► 原始hello() ──► hello3
    ├── func() ──► 原始hello() ──► hello3
    │
    └── print 函数执行后


对于闭包变量：
    n = 3，是decorator和wrapper的闭包变量

可以理解为：
    repeat
    │
    └── n = 3
            ▲
            │
            ├──── decorator 闭包需要它
            │
            └──── wrapper 闭包也需要它

大致像：
    cell
    ┌─────────┐
    │    3    │
    └─────────┘
    ▲   ▲
    │   │
    decorator
    wrapper

真实结构更接近：

    Global
    │
    ├── repeat ───────────────► function repeat
    │
    └── hello ────────────────► function wrapper
                                │
                                │ __closure__
                                ▼
                            ┌───────────────┐
                            │ cell: func    │──► 原始 hello
                            ├───────────────┤
                            │ cell: n       │──► 3
                            └───────────────┘

"""


# =============================================================


"""
为什么 @wraps(func) 后函数名仍然是原函数名？

    需要先纠正一个非常容易产生的理解：
        @wraps(func) 并没有让 wrapper 重新变成原来的函数。

    它做的是：
        把原函数的一些元数据复制到 wrapper 身上



    @wraps(func) 并没有让函数重新变回原函数；calculate 仍然指向 wrapper。
    functools.wraps 底层借助 update_wrapper() 
    把原函数的 __name__、__doc__、__annotations__ 等元数据
    复制给 wrapper，并通过 __wrapped__ 保存对原函数的引用，
    因此查看 __name__ 时仍然显示原函数名
"""

from functools import wraps

def timer(func):

    @wraps(func)    # 等价于 wrapper = wraps(func)(wrapper)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    # wrapper = wraps(func)(wrapper)

    return wrapper


@timer
def calculate():
    """执行计算"""
    return 10


print(calculate.__name__)   # calculate
print(calculate.__doc__)    # 执行计算
print(calculate.__wrapped__)    # <function calculate at 0x0000026F8EA889A0>




"""
对于上面的代码，此时calculate仍然指向wrapper，可以把wraps想象成：

    原函数 calculate
    ┌────────────────────────┐
    │ __name__ = calculate   │
    │ __doc__  = 执行计算     │
    └────────────────────────┘
                │
                │ 复制元数据
                ▼
    wrapper
    ┌────────────────────────┐
    │ __name__ = calculate   │
    │ __doc__  = 执行计算     │
    │ __wrapped__ ───────────────→ 原 calculate
    └────────────────────────┘
                ▲
                │
    calculate ───┘
"""


# -------------------------------------------------------------


"""
自己写一个简化的版本模拟wraps
"""

def my_wraps(wrapped):
    def decorator(wrapper):
        wrapper.__name__ = wrapped.__name__
        return wrapper

    return decorator


def timer(func):

    @my_wraps(func)
    def wrapper():
        func()

    # wrapper = my_wraps(func)(wrapper)

    return wrapper


@timer
def cal():
    """执行"""
    return 202


print(cal.__name__)     # cal



# =============================================================


"""
多个装饰器装饰一个函数：

    装饰时：从下往上执行。调用时：从上往下进入

"""

def deco1(func):
    def wrapper():
        print("deco1 前")
        func()
        print("deco1 后")

    return wrapper


def deco2(func):
    def wrapper():
        print("deco2 前")
        func()
        print("deco2 后")

    return wrapper


@deco1  # 后执行
@deco2  # 先执行
def hello():
    print("hello")

"""等价于"""
# hello = deco1(deco2(hello))

hello()

# 输出

    # deco1 前
    # deco2 前
    # hello
    # deco2 后
    # deco1 后