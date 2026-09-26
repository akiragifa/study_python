# print("tools 包被导入了")

from .add import add
from .multiply import multiply

"""
from . import add   导入的是add模块
from .add import add    导入的是add模块的add函数

"""

__all__ = ["add"]