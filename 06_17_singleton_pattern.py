"""
单例模式 Singleton
"""

class Config:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

a = Config()
b = Config()

print(a is b)   # True


"""

| 模式 | 解决的问题 | 核心思想 |
|---|---|---|
| 工厂模式 | **创建哪种对象** | 把创建对象集中起来 |
| 单例模式 | **创建几个对象** | 一个类只有一个实例 |




"""