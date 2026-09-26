"""
一般的项目目录：

my_project/
│
├── main.py
│
└── tools/
    ├── __init__.py
    ├── math_tools.py
    └── string_tools.py


包 package
│
├── __init__.py
├── 模块A.py
├── 模块B.py
└── ...

包本质上是用来组织多个模块的

"""

# -------------------------------------------------------------


"""
导入包时，会做以下动作：
    找到 tools 包
        ↓
    执行 tools/__init__.py
        ↓
    创建 tools 包对象


一个容易困惑的地方：
    Python 中包对象的类型同样是 module

所以：
    tools 是 package
        ↓
    但运行时对象类型属于 module
    
"""

# import tools    # 导入了包

# print(tools)    # <module 'tools' from 'e:\\study_code\\study_python\\tools\\__init__.py'>
# print(type(tools))  # <class 'module'>

"""
如果 "__init__.py" 里面是空的，那么无法直接使用module里面的函数

包里面“存在某个模块”，不等于这个模块已经被导入
"""


# -------------------------------------------------------------


# import tools.add    # 导入了包里面的某个module

# result = tools.add.add(1, 2)
# print(result)   # 3

"""
tools . add . add(10, 20)
  ↑      ↑       ↑
 包     模块     函数
"""

# -------------------------------------------------------------

"""
如果想 import tools 后直接使用函数，那么需修改 __init__.py


from .add import add
from .multiply import multiply


将 add 和 multiply 放进 tools 包的命名空间，整个过程为：
    import tools
        │
        ▼
    执行 tools/__init__.py
        │
        ├── from .add import add
        │                  │
        │                  └── add函数
        │
        └── from .multiply import multiply
                                │
                                └── multiply函数
        │
        ▼
    tools 包对象
        │
        ├── add
        └── multiply

"""

"""下面的代码是修改了 _init__.py 之后的效果"""

# import tools

# result2 = tools.add(2, 8)
# result3 = tools.multiply(2, 8)

# print(result2, result3)     # 10 16

# print(tools.add)    # <function add at 0x000001ADFCFECF40>
# print(type(tools.add))  # <class 'function'>


# -------------------------------------------------------------


"""
| 写法                          | 导入的主要对象              | 使用方式              |
| --------------------------- | -------------------- | ----------------- |
| `import tools`              | `tools` 包            | 取决于 `__init__.py` |
| `import tools.add`          | `tools.add` 模块       | `tools.add.add()` |
| `from tools import add`     | `tools` 中的 `add` 名字  | 取决于 `add` 指向什么    |
| `from tools.add import add` | `add.py` 中的 `add` 函数 | `add()`           |



若 __init__.py 什么都不写
    from tools.add import add
    from tools.multiply import multiply

若 __init__.py 写：
    from .add import add    
    from .multiply import multiply

则可直接导入
    from calculator import add, multiply


"."表示当前包

"""


"""
因此， __init__.py 最重要的用途，就是控制包对外暴露什么
"""


# -------------------------------------------------------------


"""
__all__
"""
# from tools import *     # 以*的方式导入时，只有写在 __all__ 里面的会被导入
# print(add(1, 2))
# print(multiply(1, 2))    # 报错


from tools import add, multiply  # 写明导入的内容，就算__all__里面没有，也会导入

print(add(1, 2))    # 3
print(multiply(1, 2))    # 2