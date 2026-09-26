class Car:

    category = "汽车"

    def run(self):
        print("running")



"""Car是type类的实例对象"""
print(Car)  # <class '__main__.Car'>
print(type(Car))    # <class 'type'>


# -------------------------------------------------------------

"""
Car是类对象，car1是实例对象，不是一回事

类对象最大的作用之一，就是 “保存类级别的数据和行为”

可以理解为：
    Car
    类对象
    │
    ├── category
    ├── __init__
    ├── run
    │
    └── 可以创建实例
        ↓
        car1
        实例对象
        │
        ├── brand = "BYD"
        └── mass = 2100
"""

print(Car.__dict__)     # {'category': '汽车' ,'run': <function Car.run at 0x0000025A34DB1440>, ...}

print(Car.category)     # 汽车
print(Car.run)  # <function Car.run at 0x000001AE00831440>，函数对象



Car.country = "China"
print(Car.__dict__)     # {'country': 'China', ...}

# -------------------------------------------------------------

"""甚至可以把类传给函数"""

def create_object(cls):
    return cls()


class Car:
    pass

obj = create_object(Car)
print(type(obj))    # <class '__main__.Car'>


"""类对象还能被函数返回"""

def get_class():

    class People:
        pass

    return People


MyWife = get_class()
ying = MyWife()
print(isinstance(ying, MyWife))     # True
# print(isinstance(ying, People))     # 报错，外部变量看不到People


# -------------------------------------------------------------

class Car:
    pass


"""
大致可以理解为：
"""
Car = type("Car", (), {})
print(Car)  # <class '__main__.Car'>
car = Car()
print(car)  # <__main__.Car object at 0x000002CD458E6E40>

"""
三个参数大致表示：
    "Car"
    类名

    ()
    父类

    {}
    类名称空间
"""

# -------------------------------------------------------------

class Car:

    category = "汽车"

    def __init__(self, brand):
        self.brand = brand

    def run(self):
        pass


car1 = Car("BYD")

"""
结构：
    实例对象 car1
    │
    ├── __dict__
    │     └── brand: "BYD"
    │
    └── __class__
        ↓
        Car 类对象
        │
        ├── __dict__
        │     ├── category
        │     ├── __init__
        │     └── run
        │
        └── __class__
                ↓
            type

"""

print(car1.__class__)   # <class '__main__.Car'>
print(car1.__class__ is Car)    # True
print(car1.__class__ is type)   # False


# -------------------------------------------------------------


"""
类属性
"""

class Car:

    count = 0   # 类属性

    def __init__(self, brand, mass):
        self.brand = brand
        self.mass = mass
        Car.count += 1


car1 = Car("BYD", 2100)
car2 = Car("Auto", 3300)

print(Car.count)    # 2


# -------------------------------------------------------------


"""
内存加载
"""

class Car:
    category = "汽车"       # 类属性

    def __init__(self, brand, mass):
        self.brand = brand  # 实例属性
        self.mass = mass

    def run(self):          # 实例方法
        print(self.brand)

    @classmethod
    def show_category(cls):     # 类方法
        print(cls.category)

    @staticmethod
    def add(a, b):          # 静态方法
        return a + b


car1 = Car("BYD", 2500)
car2 = Car("Toyota", 3000)

"""
    Car 类对象
    │
    ├── category ───────────────► "汽车"
    ├── __init__ ───────────────► function 对象
    ├── run ────────────────────► function 对象
    ├── show_category ──────────► classmethod 对象
    └── add ────────────────────► staticmethod 对象

实例方法、类方法、静态方法，本质上都是先作为某种对象存放在类对象的命名空间中。


"""

print(Car.__dict__)
# {
#   'category': '汽车'
#   '__init__': <function Car.__init__ at 0x000001E4B1C3CF40>
#   'run': <function Car.run at 0x000001E4B1C3CFE0>
#   'show_category': <classmethod(<function Car.show_category at 0x000001E4B1C3D080>)>
#   'add': <staticmethod(<function Car.add at 0x000001E4B1C3D120>)>
#   '__static_attributes__': ('brand', 'mass')
#   ...
# }

print(car1.__dict__)
# {
#   'brand': 'BYD'
#   'mass': 2500
# }


print(type(Car.__dict__["run"]))    # <class 'function'>
print(type(Car.__dict__["show_category"]))  # <class 'classmethod'>
print(type(Car.__dict__["add"]))    # <class 'staticmethod'>


print(type(car1.run))   # <class 'method'>
print(type(car1.show_category))     # <class 'method'>
print(type(car1.add))   # <class 'function'>


"""
类属性、实例方法、类方法、静态方法：属于Car类对象，类创建时进入内存
实例属性：实例创建之后才进入实例内存

内存关系可以想象成：

    Car 类对象
    │
    ├── category            类属性
    ├── run                 实例方法
    ├── show_category       类方法
    └── add                 静态方法


    car1 实例对象
    └── brand ───► "BYD"    实例属性


    car2 实例对象
    └── brand ───► "Toyota" 实例属性

"""

print(Car.__dict__["run"])  # <function Car.run at 0x0000019723F2CFE0>，函数对象
print(car1.run)     # <bound method Car.run of <__main__.Car object at 0x0000019723D16F90>>，绑定方法对象

print(car1.__dict__)    # {'brand': 'BYD', 'mass': 2500}，无run方法，也就是说，car1.run通常是在访问时动态产生的



"""
因此：
    函数本体
    长期存在 Car 中

    bound method
    访问 car1.run 时动态绑定产生
"""

"""
| 类型   | 在 `Car.__dict__` 中 | 访问时自动绑定什么 |
| ---- | ------------------ | --------- |
| 实例方法 | `function`         | 实例 `self` |
| 类方法  | `classmethod`      | 类 `cls`   |
| 静态方法 | `staticmethod`     | 什么都不绑定    |


"""


"""
内存关系粗略画成：

    全局命名空间
    │
    ├── Car ────────────────┐
    ├── car1 ───────────┐   │
    └── car2 ───────┐   │   │
                    │   │   │
                    ▼   ▼   ▼

                实例对象   类对象 Car
                car2       │
                │          ├── category ──► "汽车"
                └brand     ├── __init__ ──► function
                "Toyota" ├── run ───────► function
                        ├── show_category ─► classmethod
                实例对象   └── add ───────► staticmethod
                car1
                │
                └── brand ──► "BYD"

"""


# -------------------------------------------------------------

"""
    类方法：
        适合处理和整个类有关的数据
        重要用途：替代构造器
    静态方法：
        不传self，也不传cls，但如果函数逻辑上明显属于类，就应该放进类中

"""

class Car:
    category = "汽车"       # 类属性

    def __init__(self, brand, mass):
        self.brand = brand  # 实例属性
        self.mass = mass

    def run(self):          # 实例方法
        print(self.brand)

    @classmethod
    def show_category(cls):     # 类方法
        print(cls.category)

    @staticmethod
    def add(a, b):          # 静态方法
        return a + b


car1 = Car("BYD", 2500)
car2 = Car("Toyota", 3000)

car1.show_category()    # 汽车，类方法也可以通过实例调用，即使通过实例调用，传入的参数依然是Car类
"""但更推荐写"""
Car.show_category()     # 汽车