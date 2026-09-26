"""
可以把 Python 函数理解成：

把一段可以重复使用的代码封装起来，给它起一个名字，需要时通过名字调用


函数默认返回 None

"""


"""
总结：
| 类型     | 示例                 | 按什么匹配       |
| ------ | ------------------ | ----------- |
| 位置参数   | `func(10, 20)`     | 位置          |
| 关键字参数  | `func(a=10, b=20)` | 参数名         |
| 默认参数   | `def func(a=10)`   | 没传值时使用默认值   |
| 仅位置参数  | `def func(a, /)`   | 只能按位置       |
| 仅关键字参数 | `def func(*, a)`   | 只能写 `a=...` |


"""



def total(a, b):
    return a + b, a, b

a = 6
b = 4

c = total(a, b)
print(c)    # (10, 6, 4)
print(type(c))  # <class 'tuple'>，返回多个值以tuple形式返回


# -------------------------------------------------------------

"""函数默认参数，默认参数必须放在最后"""

def greet(name, message = "你好"):
    print(message, name)

greet("akiragifa")  # 你好 akiragifa


# -------------------------------------------------------------

"""
注解：
a预期是int，b预期是int
函数预期返回int

但不是强制的

"""

def add(a: int, b: int) -> int:
    """计算两个整数的和。"""
    return a + b

x = 1
y = 3

print(add(1, 3))    # 4


# -------------------------------------------------------------

"""函数位置参数"""

def print_name(name1, name2, name3):
    print(name1)
    print(name2)
    print(name3)

print_name("akiragifa", "xixi", "haha")

print_name("xixi", "haha", "akiragifa")     # 顺序与形参位置一一对应


# -------------------------------------------------------------

"""可变参数"""

def print_prop(*args):
    print(args)     # 以元组形式接收

print_prop("shell")     # ('shell',)
print_prop("shell", "solid")    # ('shell', 'solid')
print_prop("shell", "solid", "beam")    # ('shell', 'solid', 'beam')


# -------------------------------------------------------------

"""关键字参数"""

"""
关键字参数与位置参数混用时，位置参数必须在关键字参数前面

函数(
    位置参数,
    位置参数,
    关键字参数=值,
    关键字参数=值
)

"""

def prop(**kwargs):
    print(kwargs)
    print(type(kwargs))

prop()  # {}，\n <class 'dict'>，以字典类型接受
# prop(1, 2)  # 报错
prop(section = "shell", E = 210000)     # {'section': 'shell', 'E': 210000}，采用key = value形式传值



def introduce(name, age, city):
    print(f"我是{name}, 今年{age}岁，来自{city}")

introduce("akiraigfa", 18, "shenzhen")  # 我是akiraigfa, 今年18岁，来自shenzhen
introduce(age = 18, city = "xian", name = "xixi")   # 我是xixi, 今年18岁，来自xian

introduce("akira", city = "shanghai", age = 29)     # 我是akira, 今年29岁，来自shanghai
# introduce(name = "xingxing", 25, "yunan")   # 报错



"""
形参 * 后的参数必须以 关键字参数 传值

def test(a, b, *, c, d):
         │  │     │  │
         └──┘     └──┘
        普通参数   仅关键字参数

"""

def create_user(name, *, admin = False, active = True):
    print(name, admin, active)

# create_user("akiragifa", False, True)   # 报错
create_user("akiraigfa", admin = False, active = True)  # akiraigfa False True
create_user("xixi")     # xixi False True


"""
def func(a, b, /, c, d):        / 前面的参数只能通过位置传递

完整结构：
def func(a, b, /, c, d, *, e, f):
    ...

a, b
↓
只能位置传递

c, d
↓
位置或关键字都可以

e, f
↓
只能关键字传递

"""

def fun2(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# fun2(a = 1, 2, 3, 4, e = 5, f = 6)      # 报错
fun2(1, 2, 3, d = 4, e = 5, f = 6)  # 1 2 3 4 5 6



# -------------------------------------------------------------
# -------------------------------------------------------------

"""
    函数嵌套

        
"""


"""嵌套调用"""

def study():
    print("学习")

def py():
    study()
    print("python")

py()    # 学习 \n python


# -------------------------------------------------------------


"""嵌套定义：真正的嵌套函数"""

"""
嵌套函数可以：

    隐藏内部实现
    减少全局函数数量
    组织复杂逻辑
    配合闭包
    配合装饰器

"""


def outer():
    def inner():
        print("我是内部函数")

    inner()

outer()     # 我是内部函数

"""
作用域大致为：

全局作用域
│
├── outer  ← 可以看到
│
└── outer内部
    │
    └── inner ← 通常只在这里可以看到

因此，全局直接 inner() 不可以，会报错
"""





"""内部函数可以访问外部函数的变量"""

def outer2():
    name = "akira"

    def inner2():
        print(name)

    inner2()

outer2()  # akira

"""
结构为：
outer
│
├── name = "akira"
│
└── inner
      │
      └── 可以读取 name

"""


"""
Python查找变量的顺序：

LEGB 规则：L → E → G → B
    Local      局部作用域
    Enclosing  外层函数作用域
    Global     全局作用域
    Built-in   内置作用域

"""



# -------------------------------------------------------------


"""内部函数修改外部变量"""

def outer3():
    x = 10

    def inner3():
        x = 20
        print(x)

    inner3()
    print(x)

outer3()    # 20 \n 10，默认是在inner()中重新建立了一个x，内外层不是一个x


"""若想实现内层函数修改外层函数变量"""

def outer4():
    x = 10

    def inner4():
        nonlocal x
        x = 20
        print(x)

    inner4()
    print(x)

outer4()    # 20 \n 20，nonlocal表示不在inner()中创建新的x，使用外层函数的x


"""若想实现函数修改全局变量"""

x = 10

def test():
    global x
    x = 20

test()
print(x)    # 20，表示修改了全局的x变量


# -------------------------------------------------------------

"""
外部函数返回内部函数
"""

def outer5():
    def inner5():
        print("hello")
    
    return inner5   # 返回函数对象本身

func = outer5()     # 此时func就指向 inner5() 函数
func()  # hello

"""
执行过程：
    outer()
    ↓
    创建 inner 函数
    ↓
    return inner
    ↓
    func = inner
    ↓
    func()
    ↓
    调用 inner()

"""



""" 
return inner 和 return inner() 区别非常大
    return inner：返回函数本身
    return inner()：返回函数执行后的返回值

"""
def outer6():
    def inner6():
        return 100

    return inner6()

result = outer6()
print(result)   # 100