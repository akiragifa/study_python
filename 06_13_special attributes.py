"""
特殊属性


| 特殊属性              | 作用              | 常见对象     |
| ----------------- | --------------- | -------- |
| `__class__`       | 查看对象属于哪个类       | 实例、类等    |
| `__dict__`        | 查看对象自身保存的属性字典   | 实例、类、模块等 |
| `__doc__`         | 查看文档字符串         | 类、函数、模块等 |
| `__module__`      | 查看类/函数定义在哪个模块   | 类、函数     |
| `__name__`        | 对象的名称           | 类、函数、模块  |
| `__qualname__`    | 对象的限定名称         | 类、函数     |
| `__bases__`       | 查看类的直接父类        | 类        |
| `__mro__`         | 查看类的方法解析顺序      | 类        |
| `__annotations__` | 查看类型注解          | 类、函数、模块  |
| `__slots__`       | 限制实例属性、改变实例存储方式 | 类定义中     |

"""


class Vehicle:
    """交通工具"""
    pass


class Car(Vehicle):
    """汽车类"""

    category = "汽车"

    def __init__(self, brand: str, speed: float):
        self.brand = brand
        self.speed = speed

    def run(self):
        """汽车行驶"""
        print("running")


car = Car("BYD", 20)

# --------------------------

print(car.__class__)    # <class '__main__.Car'>，可以简单理解为：car.__class__ ≈ type(car)
print(car.__dict__)     # {'brand': 'BYD', 'speed': 20}


# --------------------------

print(Car.__dict__)     # 
print(Car.__name__)     # Car
print(Car.__qualname__)     # Car
print(Car.__module__)   # __main__
print(Car.__bases__)    # (<class '__main__.Vehicle'>,)
print(Car.__mro__)  # (<class '__main__.Car'>, <class '__main__.Vehicle'>, <class 'object'>)
print(Car.__doc__)  # 汽车类


# --------------------------

print(Car.run.__name__)     # run
print(Car.run.__qualname__)     # Car.run
print(Car.run.__doc__)  # 汽车行驶
print(Car.__init__.__annotations__)     # {'brand': <class 'str'>, 'speed': <class 'float'>}


"""
特殊属性
├── __class__
├── __dict__
├── __doc__
├── __name__
├── __bases__
└── __mro__

特殊方法
├── __new__()
├── __init__()
├── __str__()
├── __repr__()
├── __call__()
└── __del__()

"""