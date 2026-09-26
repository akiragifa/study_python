"""
对象的__str__方法

用来定义：
    当一个对象被转换成“给人看的字符串”时，应该显示什么内容


__str__必须返回字符串
str(obj)也会调用__str__

"""

class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


car = Car("BMW", 120)

print(car)  # <__main__.Car object at 0x000001FA49BB6BA0>


# -------------------------------------------------------------


class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f"汽车品牌：{self.brand}，速度：{self.speed}km/h"    # 必须返回字符串

car = Car("BMW", 120)

print(car)  # 汽车品牌：BMW，速度：120km/h

text = str(car)
print(text)     # 汽车品牌：BMW，速度：120km/h
print(type(text))   # <class 'str'>

print(f"我的车是：{car}")   # 我的车是：汽车品牌：BMW，速度：120km/h


"""
大致流程是：
    print(car)
        ↓
    需要把 car 转成字符串
        ↓
    str(car)
        ↓
    调用 car.__str__()
        ↓
    得到字符串
        ↓
    输出到终端
"""


# -------------------------------------------------------------

class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):  # 适合人看
        return f"汽车品牌：{self.brand}，速度：{self.speed}km/h"    # 必须返回字符串


    def __repr__(self):
        return f"Car(brand={self.brand!r}, speed={self.speed})"     # !r 会保留字符串的引号

car = Car("BMW", 120)


print(car)  # 汽车品牌：BMW，速度：120km/h，有str，默认先调str

print(str(car))     # 汽车品牌：BMW，速度：120km/h
print(repr(car))    # Car(brand=BMW, speed=120)


"""重要"""
print([car])    # [Car(brand=BMW, speed=120)]，列表展示内部元素时，通常使用元素的 repr()


car2 = Car("BYD", 200)
print(repr(car2))   # Car(brand=BYD, speed=200)
