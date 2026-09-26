"""
工厂模式

"""

class Beam:
    def create(self):
        print("创建 Beam 连接")


class Spring:
    def create(self):
        print("创建 Spring 连接")


class Rigid:
    def create(self):
        print("创建 Rigid 连接")



class ConnectionFactory:    # 把对象的创建过程集中管理

    @staticmethod
    def create(connection_type):

        if connection_type == "beam":
            return Beam()
        elif connection_type == "spring":
            return Spring()
        elif connection_type == "rigid":
            return Rigid()
        else:
            raise ValueError("未知连接类型")


"""main"""
connection = ConnectionFactory.create("beam")
connection.create()     # 创建 Beam 连接

connection = ConnectionFactory.create("spring")
connection.create()     # 创建 Spring 连接


# -------------------------------------------------------------

"""
工厂模式与多态

"""

class Connection:
    def create(self):
        raise NotImplementedError


class Beam(Connection):
    def create(self):
        print("创建Beam")


class Spring(Connection):
    def create(self):
        print("创建Spring")


class Rigid(Connection):
    def create(self):
        print("创建rigid")


class ConnectionFactory:

    @staticmethod
    def create(connection_type):
        if connection_type == "beam":
            return Beam()
        elif connection_type == "spring":
            return Spring()
        elif connection_type == "rigid":
            return Rigid()


"""main"""
connection = ConnectionFactory.create("spring")
connection.create()     # 创建Spring

"""
同一个：
    connection.create()

可能表现为：
    创建 Beam
    创建 Spring
    创建 Rigid

为多态表现
"""