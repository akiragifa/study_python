"""
继承：

1、子类可以继承什么
    父类中的大部分内容，子类都可以访问，包括：
        父类类属性：vehicle_type
        父类实例属性：brand
        父类实例方法：run()

    但要注意，实例属性 brand 并不是“直接继承过来的对象数据”，
    而是因为：Car("BYD")最终调用了父类的__init__，执行self.brand = brand
    才创建出来的

"""

class Vehicle:

    vehicle_type = "交通工具"

    def __init__(self, brand):
        self.brand = brand

    def run(self):
        print(f"{self.brand} 正在行驶")

    def ene(self):
        print("交通工具能源")



class Product:

    def show_price(self):
        return 500

    def ene(self):
        print("产品能源")




class Car(Vehicle):

    def charge(self):
        print("汽车正在充电")

    def ene(self):      # 方法重写(override)，子类重写父类方法
        print("汽车能源为电或汽油")



class Airplane(Vehicle):

    def __init__(self, brand, speed):   # __init__重写
        super().__init__(brand)
        self.speed = speed

    def run(self):
        super().run()   # 调用父类
        print(f"飞机速度提高，速度为{self.speed}")


class Bicycle(Vehicle, Product):    # 多继承
    pass


# --------------------------


car = Car("BYD")

print(car.vehicle_type)     # 交通工具
print(car.brand)    # BYD
car.run()   # BYD 正在行驶

car.charge()    # 汽车正在充电

car.ene()   # 汽车能源为电或汽油




airplane = Airplane("boyin", 800)

airplane.run()  # boyin 正在行驶 \n 飞机速度提高，速度为800




bic = Bicycle("自行车品牌")
print(bic.show_price())     # 500

bic.ene()   # 交通工具能源，父类同名方法，按照 MRO 顺序进行查找，先找Vehicle类，再找Product类，找到就停止
print(Bicycle.__mro__)  # (<class '__main__.Bicycle'>, <class '__main__.Vehicle'>, <class '__main__.Product'>, <class 'object'>)


# --------------------------

"""
issubclass()：判断两个类是否是继承关系
"""

print(issubclass(Car, Vehicle))     # True
print(issubclass(Car, Product))     # False

print(issubclass(Bicycle, Vehicle))     # True
print(issubclass(Bicycle, Product))     # True


# -------------------------------------------------------------

print(dir(object))
# [
#    '__class__', 
#    '__delattr__', 
#    '__dir__', 
#    '__doc__', 
#    '__eq__', 
#    '__format__', 
#    '__ge__', 
#    '__getattribute__', 
#    '__getstate__', 
#    '__gt__', 
#    '__hash__', 
#    '__init__', 
#    '__init_subclass__', 
#    '__le__', 
#    '__lt__', 
#    '__ne__', 
#    '__new__', 
#    '__reduce__', 
#    '__reduce_ex__', 
#    '__repr__', 
#    '__setattr__', 
#    '__sizeof__', 
#    '__str__', 
#    '__subclasshook__'
# ]

print(dir(car))

"""相比object，多出来8个"""
# [
#    '__dict__',, 
#    '__firstlineno__', 
#    '__module__', 
#    '__static_attributes__', 
#    '__weakref__', 
#    'brand', 
#    'charge', 
#    'ene', 
#    'run', 
#    'vehicle_type'
# ]


# -------------------------------------------------------------

"""
菱形继承：

        A
       / \
      B   C
       \ /
        D

"""

class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()


d = D()
# D init
# B init
# C init
# A init

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# D -> B -> C -> A向后找，因此，B不直接找A，而是会先找C，因此可以输出 “c init”