"""
字符串类型

单双引号均可
双引号更常用
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


part_name = "door_inner_panel"
print(part_name.split("_"))     # ['door', 'inner', 'panel']    # 分割
print(type(part_name.split("_")))   # <class 'list'>

# -------------------------------------------------------------

"""
字符串格式化
"""

mass = 1500
output = f"Vehicle mass is {mass} kg"
print(output)   # Vehicle mass is 1500 kg