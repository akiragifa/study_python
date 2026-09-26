"""
Python 里所谓“私有属性”和“私有方法”，核心是：不希望类外部直接访问的成员。
但要注意，Python 的“私有”并不像 Java、C++ 那样是强制禁止访问，
而主要依赖一种叫 名称改写（name mangling） 的机制。

最常见的写法，是在属性或方法名前加两个下划线 __

Python 的私有属性和私有方法不是“禁止外部访问”，而是通过 name mangling 降低误访问和名称冲突的可能性。


"""

class Car:

    def __init__(self, brand, speed):
        self.brand = brand      # 实例属性
        self.__speed = speed    # 私有属性


    def __show_speed(self):
        print(f"当前速度：{self.__speed}")


    def show_info(self):
        print(self.brand)
        self.__show_speed()


car = Car("BYD", 35)

print(car.brand)    # BYD
# print(car.__speed)  # 报错，'Car' object has no attribute '__speed'

# 但实际上，只是python在创建类时，会把 __speed 改写成 _Car.__speed

print(car._Car__speed)  # 35，只是不建议这样调用

"""
这样设计的目的：
    1、告诉别人“这是类内部实现，不要随便用”；
    2、防止子类无意中覆盖父类属性

"""

# -------------------------------------------------------------

class A:

    def __init__(self):
        self.__value = 10



class B(A):

    def __init__(self):
        super().__init__()
        self.__value = 20


b = B()
print(b.__dict__)   # {'_A__value': 10, '_B__value': 20}

# -------------------------------------------------------------

"""
_speed：单下划线，没有强制改写名称，只是程序员间的约定，这个成员属于内部使用，不要随便访问
__speed：python会进行名称改写（name mangling）

"""

# -------------------------------------------------------------

"""
实际开发中，私有属性一般通过方法访问

"""

class Car:

    def __init__(self, speed):
        self.__speed = speed


    def get_speed(self):
        return self.__speed


    def set_speed(self, value):
        if value >= 0:
            self.__speed = value


car = Car(100)
print(car.get_speed())  # 100

car.set_speed(120)
print(car.get_speed())  # 120


# -------------------------------------------------------------

"""
python对于这种 get / set 方法，更常用的是使用 @property

"""

class Car:

    def __init__(self, speed):
        self.__speed = speed


    @property
    def speed(self):
        return self.__speed


    @speed.setter
    def speed(self, value):

        if value <= 0:
            raise ValueError("速度不能小于0")

        self.__speed = value


car = Car(100)
print(car.speed)    # 100

car.speed = 120
print(car.speed)    # 120

# -------------------------------------------------------------


"""
完整例子
"""

class Car:

    car_type = "汽车"

    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed

    def __show_speed(self):
        print(f"速度：{self.__speed}")


    def show_info(self):
        print(f"品牌：{self.brand}")
        self.__show_speed()


car = Car("BYD", 100)

print(car.__dict__)     # {'brand': 'BYD', '_Car__speed': 100}
print(Car.__dict__)     # '_Car__show_speed': <function Car.__show_speed at 0x000001E43C15D4E0>, 'show_info': <function Car.show_info at 0x000001E43C15D580> ...

car.show_info()     # 品牌：BYD \n 速度：100

car.show_type()     # 类型：汽车