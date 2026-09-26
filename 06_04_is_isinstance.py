"""
可以把 is 和 isinstance() 看成是在回答两个完全不同的问题：

==：值是否相等
is：是不是同一个对象，实际上比较id是否相同，id(a) == id(b)
isinstance()：是不是某种类型的对象


总结：
    ==           看“值”
    is           看“是不是同一个对象”
    isinstance   看“对象是什么类型”

"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]


print(id(a))    # 2164313251904，其中一种输出
print(id(b))    # 2164313251904，其中一种输出
print(id(c))    # 2164313401984，其中一种输出

print(a == b)   # True
print(a is b)   # True

print(a == c)   # True
print(a is c)   # False


"""
a ─────┐
       ▼
    [1, 2, 3]
       ▲
b ─────┘


c ─────► [1, 2, 3]

"""

# --------------------------

"""
实际开发里面，is常用于判断None
    if x is None
而不是写：
    if x == None

这是因为 None 是一个特殊的单例对象，
Python运行时，关心的是这个变量是不是指向唯一的None对象
"""

x = None
print(x is None)    # True
print(x is not None)    # False

# =============================================================

"""
isinstance()

"""

m = 10
print(isinstance(m, int))   # True，意思是：m是否是int的实例对象

# --------------------------

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True

print(type(dog))    # <class '__main__.Dog'>
print(type(dog) == Dog)     # True
print(type(dog) == Animal)  # False


"""
总结：
    | 写法                      | 判断什么                  |
    | ----------------------- | --------------------- |
    | `type(x) is Dog`        | x 的实际类型是不是恰好就是 Dog    |
    | `isinstance(x, Dog)`    | x 是不是 Dog 或 Dog 子类的实例 |
    | `isinstance(x, Animal)` | x 是否属于 Animal 这条继承体系  |


"""


# --------------------------

"""
isinstance()同时判断多个类型

"""

y = 10

print(isinstance(y, (int, float)))  # True，判断y是否是 int 或  float 类型


# --------------------------

"""
注意：bool是int的子类，继承关系：

    object
    ↑
    int
    ↑
    bool

"""

print(isinstance(True, bool))   # True
print(isinstance(True, int))    # True