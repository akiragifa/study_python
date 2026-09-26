"""
自定义对象的深浅拷贝

浅拷贝：创建一个新的外层对象，但对象内部引用的子对象仍然共用。
深拷贝：创建一个新的外层对象，并递归复制内部对象。
"""

import copy

class Car:
    def __init__(self, brand, parts):
        self.brand = brand
        self.parts = parts


car1 = Car("BMW", ["wheel", "engine"])

"""
car1:
    car1
    │
    ▼
    Car对象
    ├── brand ─────→ "BMW"
    │
    └── parts ─────→ ["wheel", "engine"]
"""


car2 = copy.copy(car1)


print(car1 is car2)     # False
print(car1.brand is car2.brand)     # True
print(car1.parts is car2.parts)     # True

# --------------------------

car3 = copy.deepcopy(car1)

print(car1 is car3)     # False
print(car1.brand is car3.brand)     # True
print(car1.parts is car3.parts)     # False


# -------------------------------------------------------------

print("# --------------------------")


"""
自定义对象里面又嵌套自定义对象
"""

class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine


engine = Engine(300)
car11 = Car("BMW", engine)

car12 = copy.copy(car11)


print(car11 is car12)   # False
print(car11.engine is car12.engine)     # True

car12.engine.power = 500
print(car11.engine.power)   # 500


# --------------------------

car13 = copy.deepcopy(car11)


print(car11.__dict__)
print(car12.__dict__)
print(car13.__dict__)


# --------------------------

# engine2 = Engine(["piston", "crankshaft"])    # 三层嵌套原理一样
