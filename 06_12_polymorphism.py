"""
多态：

    同一个调用方式，面对不同对象时，可以表现出不同的行为


多态是方法的多态，属性没有多态
python实现多态，并不强制要求多个类必须继承同一个父类

其中 Python 的多态最核心的两个关键词就是：
    方法重写 + 鸭子类型

"""

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵")


def make_sound(animal):
    animal.speak()


make_sound(Dog())   # 汪汪
make_sound(Cat())   # 喵喵

"""
可以理解成：

    Animal
    ├── Dog
    │   └── speak() → 汪汪
    │
    └── Cat
        └── speak() → 喵喵


继承
↓
方法重写
↓
不同子类拥有不同实现
↓
统一接口调用不同实现
↓
形成多态
"""

# -------------------------------------------------------------


"""
工程化实例
"""

class solver:
    def solve(self):
        pass

class AbaqusSolver:
    def solve(self):
        print("调用Abaqus求解")

class LSDynaSolver:
    def solve(self):
        print("调用LS-DYNA求解")

class NastranSolver:
    def solve(self):
        print("调用Nastran求解")


def run_solver(solver):
    solver.solve()


run_solver(AbaqusSolver())  # 调用Abaqus求解
run_solver(LSDynaSolver())  # 调用LS-DYNA求解
run_solver(NastranSolver())     # 调用Nastran求解


# -------------------------------------------------------------


"""
python的多态比Java、C更自由，因为python是动态类型语言

"""

class Dog:
    def speak(self):
        print("汪汪")


class Robot:
    def speak(self):
        print("电子音")



def make_sound(obj):
    obj.speak()


# -------------------------------------------------------------


"""
鸭子类型
    经典说法是：
        如果它走起来像鸭子，叫起来像鸭子，那就把它当鸭子。

    在 Python 里就是：
        
    
Python 通常更关注“你能做什么”，而不是“你是什么”
例如传统思路可能会写：
    if isinstance(obj, Dog):
        obj.speak()
    elif isinstance(obj, Cat):
        obj.speak()

Python 更倾向：
    obj.speak()

只要对象支持就行，也就是说：
    传统思维：
        你是不是 Dog？

    Python 鸭子类型：
        你会不会 speak()？

这是一个非常重要的思想转变

"""


"""
大型项目里，有时为了规范接口，会定义抽象基类

"""

from abc import ABC, abstractmethod     # Abstract Base Class 的缩写

class Solver(ABC):  # Solver是一个抽象基类

    @abstractmethod
    def solve(self):    # 抽象方法，这样就要求 Solver 的子类都必须实现 solve()
        pass



solve = Solver()    
# 报错，存在抽象方法，不能实例化
# TypeError: Can't instantiate abstract class Solver without an implementation for abstract method 'solve'


"""
可以记为：
    Animal
    │
    │ 有抽象方法 speak()
    │
    │ 不能实例化
    │
    ├── Dog
    │    │
    │    │ 没有实现 speak()
    │    │
    │    └── 仍然是抽象类
    │
    └── Cat
        │
        │ 实现 speak()
        │
        └── 成为具体类，可以实例化

"""

"""
子类实现 speak()，只会让这个子类变成可以实例化的具体类，并不会反过来修改父类 Animal

一个类只要还有未实现的抽象方法，就不能实例化；所有抽象方法都被实现后，它就成为可以实例化的具体类。

"""