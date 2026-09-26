"""
面向对象，就是把程序中的数据和操作这些数据的功能组织成一个个“对象”

面向对象的3大特征

| 特征 | 核心含义              |
| -- | ----------------- |
| 封装 | 把数据和方法包装起来，隐藏内部实现 |
| 继承 | 子类复用父类的属性和方法      |
| 多态 | 同一个接口，不同对象有不同表现   |

"""

class Car:

    brand_type = "汽车"     # 类属性

    def __init__(self, brand, mass):    # 特殊方法
        self.brand = brand      # 实例属性
        self.mass = mass    # 实例属性
        self.speed = 0      # 实例属性

    def accelerate(self, value):    # 实例方法
        self.speed += value

    def show_info(self):    # 实例方法
        print(self.brand)
        print(self.mass)
        print(self.speed)



car1 = Car("BYD", 2100)
car2 = Car("Auto", 3600)

"""
创建对象后，Python会调用 __init__() 进行初始化，可以先粗略理解成：
    Car("BYD", 2100)
            ↓
    创建 Car 对象
            ↓
    调用 __init__()
            ↓
    给这个对象设置：
        brand = "BYD"
        mass = 2100

self可以理解成：
    当前正在操作的那个实例对象（当前实例对象本身）

"""

# --------------------------

"""
类属性
    属于Car类，所有实例都可以访问

                Car
                │
            category="汽车"
            /         \
            ↓           ↓
        car1           car2

"""
print(Car.brand_type)   # 汽车
print(car1.brand_type)  # 汽车
print(car2.brand_type)  # 汽车

# --------------------------

"""
实例属性
"""
print(car1.brand)   # BYD
print(car2.brand)   # Auto

# --------------------------

"""
实例方法
    定义时有 "self"，但是调用时只传1个参数，
    是因为通过实例调用方法时，Python 会自动把 "car1" 作为第一个参数传进去
"""
car1.accelerate(20)     # 可近似理解成 Car.accelerate(car1, 20)
car1.show_info()    # BYD \n 2100 \n 20


# -------------------------------------------------------------

"""
类本身也是对象
    Car 本身也是一个对象
    Car 是type类的实例

关系：
    type
    │
    │ 创建
    ↓
    Car
    │
    │ 创建
    ↓
    car1

"""
print(type(Car))    # <class 'type'>
print(type(car1))   # <class '__main__.Car'>



"""
总结：

Python 类
│
├── class
│     定义类
│
├── 对象 / 实例
│     Car()
│
├── 属性
│   │
│   ├── 类属性
│   │     Car.category
│   │
│   └── 实例属性
│         car.brand
│
└── 方法
    │
    └── 实例方法
          car.accelerate()


--------------------------


2个核心机制：
    __init__
        │
        └── 初始化实例对象

    self
        │
        └── 当前实例对象


--------------------------


整个过程可以理解为：
                    Car
                     │
              ┌──────┴──────┐
              │             │
           类属性           方法
              │             │
      category="汽车"    __init__()
                            │
                            │ Car("BYD", 2100)
                            ↓
                           car1
                            │
                     ┌──────┼──────┐
                     ↓      ↓      ↓
                   brand   mass   speed
                    BYD    2100     0

"""