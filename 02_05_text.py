"""
字符串类型

单双引号均可
双引号更常用
"""

"""
常用函数:
+：字符串拼接
*: 重复输出
len：字符串长度
[]：索引
[0:3]：切片，取0-3的左开右闭片段
upper()：转大写
lower()：转小写
strip()：去空格
replace()：代替
split()：分割

成员运算符：
    in
    not in

索引：索引从0开始

查找：find，查找子字符串是否在字符串中，如果在则返回索引，不在返回-1
     index，类似于find，但找不到报错

计数：count，返回子字符串出现的次数

判断：startswith  endswith，判断是否以某字符开头/结尾
      isupper   islower，判断所有字母是否都为大写/小写

capitalize：第一个字符大写，其余字母全部小写

修改：
    replace


"""



material = "steel"
print(type(material))   # <class 'str'>


rho = "100"
print(type(rho))    # <class 'str'>

# -------------------------------------------------------------

"""
字符串拼接
"""

print(rho + rho)    # 100100，表示字符串拼接


first = "LS"
second = "DYNA"

name = first + "-" + second

print(name)     # LS-DYNA
print(type(name))   # <class 'str'>


# -------------------------------------------------------------

"""
字符串拼接
"""

print("akiragifa\t" * 3)  # akiragifaakiragifaakiragifa

# -------------------------------------------------------------

"""
字符串长度，索引
"""

text = "Python"

print(len(text))    # 6，获取字符串长度 len()
print(text[0])    # P，访问字符串，索引从0开始
print(type(text[0]))    # <class 'str'>

# -------------------------------------------------------------

"""
字符串切片
"""

print(text[0:3])    # Pyt，左开右闭区间
print(type(text[0:3]))  # <class 'str'>

print("后切片：", text[1: ])    # 后切片： ython，取索引1及之后的所有
print("前切片：", text[: 3])    # 前切片： Pyt，取索引3之前的所有，不包括3

"""
字符：   P   y   t   h   o   n
正索引： 0   1   2   3   4   5
负索引：-6  -5  -4  -3  -2  -1
"""

print(text[-1: -3])     # ""，默认只能从左向右切，从-1开始向右，但-3在-1左边，因此取不到任何值
print(text[-1: -3: -1])     # no，从-1向左切到-3，顺序也会颠倒

print(text[-3: -1])     # ho

print(text[-1: ])   # n，表示从-1索引切片到字符串末尾
print(text[: -1])   # Pytho，表示从头切到-1索引，但不包括-1索引

# -------------------------------------------------------------

"""
常用函数
"""

print(text.upper())     # PYTHON，转大写
print(text.lower())     # python，转小写


software = " ls dyna "
print(software)     #  ls dyna
print(software.strip())     # ls dyna，去空格


print(software.replace("l", "ANSA"))    #  ANSAs dyna，替换


"""

(method) def split(
    sep: LiteralString | None = None,
    maxsplit: SupportsIndex = -1
) -> list[LiteralString]

"""

part_name = "door_inner_panel"
print(part_name.split("_"))     # ['door', 'inner', 'panel']    # 分割
print(type(part_name.split("_")))   # <class 'list'>

sub_name = part_name.split(",")
print(sub_name)     # ['door_inner_panel']
print(type(sub_name))   # <class 'list'>


# -------------------------------------------------------------

"""
成员运算符
"""

nums = [1, 2, 3, 4]
print(1 in nums)    # True
print(10 in nums)   # False

print(1 not in nums)    # False
print(10 not in nums)   # True


my_name = "akiragifa"
print("akira" in name)  # True


# -------------------------------------------------------------

"""
索引
"""

your_name = "hahaha"

print(your_name[0])     # h


# -------------------------------------------------------------

"""
查找 find

(method) def find(
    sub: str,
    start: SupportsIndex | None = None,
    end: SupportsIndex | None = None,
    /
) -> int

"""

school = "xibei gongye daxue"

print(school.find("ei go"))   # 3，返回找到的子字符串第一个位置的索引
print(school.find("e", 5, 11))      # -1，school[5, 11]左闭右开区间内找 "e"
print(school.find("e", 5, 12))      # 11


"""
查找 index

(method) def index(
    sub: str,
    start: SupportsIndex | None = None,
    end: SupportsIndex | None = None,
    /
) -> int

"""

print(school.index("ei go"))    # 3
# print(school.index("eio"))  # 报错


# -------------------------------------------------------------

"""
计数 count

(method) def count(
    sub: str,
    start: SupportsIndex | None = None,
    end: SupportsIndex | None = None,
    /
) -> int

"""

str2 = "xing xing"
print(str2.count("a"))  # 0
print(str2.count("x"))  # 2
print(str2.count("x", 1, 8))    # 1


# -------------------------------------------------------------

"""
判断 startswith  endswith

(method) def startswith(
    prefix: str | tuple[str, ...],
    start: SupportsIndex | None = None,
    end: SupportsIndex | None = None,
    /
) -> bool


(method) def endswith(
    suffix: str | tuple[str, ...],
    start: SupportsIndex | None = None,
    end: SupportsIndex | None = None,
    /
) -> bool

"""

str3 = "akiragifa"
print(str3.startswith("aki"))     # True
print(str3.startswith(("aki", "haha", "xixi")))     # True，以字符元组任意一个字符串开头，就返回True
print(str3.startswith("ir", 2, 6))  # True，切片后的字符串是否以 "ir" 开头


print(str3.endswith("aki"))     # False
print(str3.endswith(("aki", "haha", "xixi")))     # False


"""
判断 isupper  islower

(method) def isupper() -> bool

(method) def islower() -> bool

"""

str4 = "akiragifa"
print(str4.isupper())   # False
print(str4.islower())   # True


# -------------------------------------------------------------

"""
首字母大写

(method) def capitalize() -> LiteralString

"""

print("akira gifa".capitalize())     # Akira gifa
print("akira GIFA".capitalize())     # Akira gifa


# -------------------------------------------------------------

"""
修改  replace：返回一个新的替换后的字符串，而不会改变原字符串，count默认为-1，表示全部替换

def replace(
    old: str,
    new: str,
    /,
    count: SupportsIndex = -1
) -> str: ...

"""

str5 = "xingxing"
print(str5.replace("xingxing", "chen"))     # chen
print(str5)     # xingxing


str6 = "apple apple apple banana orange"
print(str6.replace("apple", "pencil", 2))