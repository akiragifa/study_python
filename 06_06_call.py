"""
__call__ 是 Python 里一个很重要的特殊方法，它决定了：

一个对象能不能像函数一样被 () 调用




可以把 Python 的调用机制总结成一句话：

x(...) 的本质，是去执行“x 的类型提供的调用行为”


"""

class MyClass:

    def __call__(self):
        print("对象被调用了")


obj = MyClass()

obj()   # 对象被调用了，实际调用的__call__方法，等价于
obj.__call__()  # 对象被调用了

# -------------------------------------------------------------

"""__call__方法可传参数"""

class Person:

    def __init__(self, name):
        self.name = name

    def __call__(self, message):
        print(f"{self.name}: {message}")


p = Person("akiragifa")
p("hello")    # akiragifa: hello

# -------------------------------------------------------------

"""
为什么需要__call__：
    它最大的价值是：

    让“有状态的对象”拥有函数一样的调用方式
"""

class Counter:

    def __init__(self):
        self.count = 0


    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()

print(counter())    # 1
print(counter())    # 2
print(counter())    # 3

# -------------------------------------------------------------

"""
callable() 与 __call__

    callable()通常用来判断一个对象是否可调用
"""

class A:
    pass

class B:

    def __call__(self):
        pass


a = A()
b = B()

print(callable(a))  # False
print(callable(b))  # True