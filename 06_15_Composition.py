"""
Python 里的组合（Composition），可以理解为：

一个对象内部，持有另一个对象，并通过这个对象来完成一部分功能。

它解决的是 “A 有一个 B（has-a）” 的关系；而继承解决的是 “A 是一种 B（is-a）” 的关系。

比如：

汽车 有一个 发动机 → 组合
电动车 是一种 汽车 → 继承

"""

"""
Python 的组合，就是把另一个类的对象作为当前对象的实例属性，
从而让当前对象使用另一个对象提供的功能
"""


class Engine:
    def start(self):
        print("发动机启动")


class Car:
    def __init__(self):
        self.engine = Engine()


    def strat(self):
        self.engine.start()
        print("汽车启动")


car = Car()

car.strat()     # 发动机启动 \n 汽车启动


# -------------------------------------------------------------


print("# --------------------------")

"""
组合 + 多态
"""

class GasEngine:
    def start(self):
        print("燃油发动机启动")


class ElectricMotor:
    def start(self):
        print("电机启动")


class Car:
    def __init__(self, power):
        self.power = power

    def start(self):
        self.power.start()


car1 = Car(GasEngine())
car2 = Car(ElectricMotor())

car1.start()  # 燃油发动机启动
car2.start()  # 电机启动


# --------------------------


class Materail:
    def __init__(self, name):
        self.name = name


class Mesh:
    def __init__(self, element_count):
        self.element_count = element_count


class Model:
    def __init__(self, material, mesh):
        self.material = material
        self.mesh = mesh


material = Materail("2000HS")
mesh = Mesh(1000000)

model = Model(material, mesh)

print(model.material.name)  # 2000HS
print(model.mesh.element_count)     # 1000000

"""
这种设计比把所有东西全部塞进一个巨大 Model 类里更容易维护
"""

# -------------------------------------------------------------

"""
实际开发中经常说“组合优于继承”      Favor composition over inheritance

不是说继承不好，而是继承关系比较强
"""