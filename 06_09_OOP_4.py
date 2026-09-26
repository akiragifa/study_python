"""
面向对象的3大特征

| 特征 | 核心含义              |
| -- | ----------------- |
| 封装 | 把数据和方法包装起来，隐藏内部实现 |
| 继承 | 子类复用父类的属性和方法      |
| 多态 | 同一个接口，不同对象有不同表现   |


"""

"""
封装：

    _speed是内部数据，speed是对外访问接口
"""
class Car:

    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed


"""
继承：
"""

class Vehicle:

    def run(self):
        print("车辆行驶")


class Car(Vehicle):
    pass


car = Car()
car.run()   # 车辆行驶


"""
多态：
"""

