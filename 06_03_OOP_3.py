class Car:

    def __init__(self, brand):
        self.brand = brand


car1 = Car("BYD")
car2 = Car("Auto")

car1.mass = 1200

print(car1.mass)    # 1200，car1实例新增加的属性
# print(car2.mass)  # 报错，'Car' object has no attribute 'mass'，car2没有mass属性


# del car1    # 删除对象


"""dir(对象)：这个对象有哪些属性和方法"""
print(dir(car1))    # ['brand', 'mass', ...]


"""__dict__：对象的自定义属性字典"""
print(car1.__dict__)    # {'brand': 'BYD', 'mass': 1200}