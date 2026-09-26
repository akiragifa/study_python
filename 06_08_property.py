"""
@property
把一个“方法”，伪装成一个“属性”来访问

"""


"""
property 有一个非常重要的设计价值：

今天看起来只是普通属性，未来可以升级成带逻辑的属性，而不改变外部调用方式

"""

class Car:

    def __init__(self, speed):
        self._speed = speed     # 实例属性_speed，修饰方法名speed，这样写初始化不会经过setter校核


    @property
    def speed(self):
        return self._speed


    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("速度不能小于0")

        self._speed = value


    @speed.deleter
    def speed(self):
        del self._speed


car = Car(100)

print(car.speed)    # 100，实际调用 @preperty
print(car.__dict__)     # {'_speed': 100}

car.speed = 120     # 实际触发 @speed.setter

del car.speed       # 实际触发 @speed.deleter

""""
理解为：
    car.speed
        ↓
    getter

    car.speed = 120
        ↓
    setter

    del car.speed
        ↓
    deleter


car
│
├── _speed = 100          ← 真正存储的数据
│
└── speed                 ← property 接口
       │
       └── return self._speed
"""


"""
最重要链条：

    @property
        ↓
    把 getter 函数交给 property()
        ↓
    生成 property 对象
        ↓
    property 对象保存在类对象中
        ↓
    car.speed
        ↓
    Python 找到 Car.speed 这个 property
        ↓
    调用 getter
        ↓
    getter 再读取 self._speed
"""

# -------------------------------------------------------------


"""
真实示例：
"""

class Car:

    def __init__(self, speed):
        self.speed = speed      # 实例与方法同名，这样写初始化会经过setter校核

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("速度不能小于0")

        self._speed = value


# car = Car(-100)     # 速度不能小于0，报错

car = Car(20)

print(Car.__dict__)     # 'speed': <property object at 0x000002F388425530>,
print(car.__dict__)     # {'_speed': 20}

print(car._speed)   # 20，但真实不会这样写
print(car.speed)    # 20


print(Car.speed.fget)   # <function Car.speed at 0x0000020EB17CCEA0>
print(Car.speed.fset)   # <function Car.speed at 0x0000020EB17CCF40>

"""
真实初始化链条为：
    Car(100)

    ↓
    __init__(self, 100)

    ↓
    self.speed = 100

    ↓
    发现 Car.speed 是 property

    ↓
    调用 setter

    ↓
    self._speed = 100


工程上更推荐：
    外部接口              内部存储
    speed      →        _speed
"""

"""
最准确的解释是：

先产生：
    speed property
    │
    ├── getter
    └── setter = None

然后变成：
    speed property
    │
    ├── getter
    └── setter


最后：
类里面：
    Car
    │
    └── speed → property
                ├── fget
                └── fset

实例里面：
    car
    │
    └── _speed → 100
"""


"""
调用 car.speed ，路线是：

        car.speed
        → Car.speed(property)
        → fget(car)
        → car._speed
        → 100


调用 car.speed = 200 ，路线是：
        car.speed = 200
        → Car.speed(property)
        → fset(car, 200)
        → car._speed = 200

"""


"""
所以你现在可以把 property 记成一句非常准确的话：

speed 是定义在类里的“属性访问接口”，
_speed 才是实例里真正保存数据的位置；
getter 和 setter 都被装进同一个 property 对象中

"""