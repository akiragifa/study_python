
# car1 = Car("BYD", 2100)

"""
当创建一个实例时，python到底经历了什么：一个核心主线

    Car("BYD", 2100)
        ↓
    调用类对象 Car
        ↓
    先执行 __new__()
        ↓
    创建一个 Car 实例对象
        ↓
    把这个对象传给 __init__()
        ↓
    __init__ 给对象设置属性
        ↓
    最终返回这个对象
        ↓
    car1 指向这个对象

__new__ 负责“创建对象”，__init__ 负责“初始化对象”


完整流程：
    Car("BYD", 2100)
            ↓
    __new__()
            ↓
    创建对象 obj
            ↓
    return obj
            ↓
    __init__(obj, "BYD", 2100)
            ↑
            self


"""

"""
| 对比        | `__new__` | `__init__` |
| --------- | --------- | ---------- |
| 主要作用      | 创建对象      | 初始化对象      |
| 第一个参数     | `cls`     | `self`     |
| `cls` 是谁  | 当前类       | —          |
| `self` 是谁 | —         | 已创建的实例     |
| 是否需要返回对象  | 是         | 不需要        |
| 常用程度      | 少         | 非常常用       |



"""

class Car:

    def __new__(cls, brand, mass):  # cls指当前这个类（Car）
        print("执行 __new__")
        obj = super().__new__(cls)  # 真正创建实例对象，super()去父类那里找对应方法，object.__new__(cls)
        print("创建出的对象：", obj)
        return obj  # 返回对象给Python


    def __init__(self, brand, mass):
        print("执行 __init__")
        self.brand = brand
        self.mass = mass


car1 = Car("BYD", 2100)

"""
Python 先通过 __new__ 创建一个 Car 实例，
再把这个实例作为 self 传给 __init__ 完成初始化，
最后让 car1 指向这个实例。
"""

"""
1° 遇到Car(...)，实际上是触发了type所定义的“类调用机制”

2° Python调用 __new__
    对于上面的代码，会导致： Car.__new__(Car, "BYD", 2000)

3° __new__真正创建实例对象，obj = super().__new__(cls)，但运行完后只是“刚出生的Car对象”，还没有实例属性
    还未初始化

4° __new__返回对象，__new__ 的返回值决定了后面要初始化哪个对象

5° 把 __new__ 创建的对象传给 __init__，类似于 Car.__init__(obj, "BYD", 2100)
    self  → obj
    brand → "BYD"
    mass  → 2100

    也就是说：
        __new__ 创建出来的对象
                │
                ↓
                obj
                │
                └──────► 作为 self 传进 __init__

    self就是 __new__创建并返回的实例对象

6° __init__ 初始化对象

7° 最终赋值给car1，car1 保存了对这个对象的引用
    car1
    │
    │ 引用
    ↓
    Car instance
    │
    ├── brand = "BYD"
    └── mass = 2100

"""


"""
从理解的角度，可粗略展开成：

    obj = Car.__new__(Car, "BYD", 2100)

    Car.__init__(obj, "BYD", 2100)

    car1 = obj

"""

"""
为什么平时很少写 __new__？

类最终继承自 object，
Class Car 基本可以理解成 Class Car(object)

如果不自己定义 __new__()
Python会使用继承来的对象创建机制，
所以一直在使用 __new__，只是不用自己写

"""


# -------------------------------------------------------------

"""
4° __new__返回对象，__new__ 的返回值决定了后面要初始化哪个对象

对这句话的理解:
    如果 __new__() 返回的是当前类 cls 的实例或其子类实例，
    那么 Python 会把这个返回对象传给 __init__() 作为 self；
    如果返回的不是 cls 的实例，
    则不会调用该类的 __init__()。

正常情况下：
    __new__ 返回的 Car 实例
            =
    __init__ 中的 self
            =
    最终 car1 指向的对象

"""

class People:
    def __new__(cls, name):
        print("执行 __new__")
        return 100

    def __init__(self, name):
        print("执行 __init__")
        self.name = name

man = People("akiragifa")   # 执行 __new__，不执行 __init__

print(isinstance(100, People)) # False

print(man)  # 100

"""
__new__返回的是100，是int类型，而不是People实例，

Python会判断，__new__返回的对象，是不是People类型的实例

isinstance(100, People)，显然是 False，后续就不会再执行 __init__

最终直接 man = 100

"""


# -------------------------------------------------------------

"""
self和obj是一个对象

    obj：__new__()里的局部变量名
    ↓
    作为实参传入
    ↓
    self：__init__的形参名


Python把__new__()返回的那个对象，作为第一个实参传给了 __init__()。
因此obj和self指向的是同一个对象，只是这个传参过程是Python的类调用机制自动完成的
真正负责协调这个过程的是 type.__call__()

关键链条是：
    __new__ 返回 obj
            ↓
    type.__call__ 拿到这个返回值
            ↓
    把 obj 作为第一个实参传给 __init__
            ↓
    __init__ 的第一个形参 self 接收到 obj
"""

class Car2:

    def __new__(cls, brand):
        obj = super().__new__(cls)
        print("__new__创建：", id(obj))
        return obj 


    def __init__(self, brand):
        print("__init__收到：", id(self))
        self.brand = brand

car = Car2("BYD")   
# __new__创建： 1795904728640
# __init__收到： 1795904728640


"""
type.__call__() 先把参数交给 __new__()；
__new__() 返回对象后，控制权回到 type.__call__()；
然后 type.__call__() 再把对象和同一批参数交给 __init__()。

"""