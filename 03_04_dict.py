"""
Python 常见内置数据类型
│
├─ 数值类型
│  ├─ int
│  ├─ float
│  └─ complex
│
├─ 布尔类型
│  └─ bool
│
├─ 序列类型
│  ├─ str
│  ├─ list
│  ├─ tuple
│  └─ range
│
├─ 映射类型
│  └─ dict
│
├─ 集合类型
│  ├─ set
│  └─ frozenset
│
└─ 空值类型
   └─ None

"""


"""
字典：
key值唯一，value可重复

增
删
改
查

"""

shell_property = {
    "ELEFOM": 16,
    "thickness": 2,
    "NIP": 5
}

print(shell_property)   # {'ELEFOM': 16, 'thickness': 2, 'NIP': 5}
print(type(shell_property))     # <class 'dict'>


# -------------------------------------------------------------

"""根据key取value"""
print(shell_property["ELEFOM"])     # 16
# print(shell_property["MAT"])    # 报错，无此key

print(shell_property.get("MAT"))    # None，无此key值返回None
print(shell_property.get("MAT", "无材料"))  # 无材料


# -------------------------------------------------------------

"""修改"""
shell_property["ELEFOM"] = 2
print(shell_property)   # {'ELEFOM': 2, 'thickness': 2, 'NIP': 5}


# -------------------------------------------------------------

"""新增，与修改一致，key存在修改，key不存在新增"""
shell_property["SHRF"] = 0.833
print(shell_property)   # {'ELEFOM': 2, 'thickness': 2, 'NIP': 5, 'SHRF': 0.833}


# -------------------------------------------------------------

"""
删除
del
clear：清空整个字典，空字典
pop：删除指定键值对

"""

solid_mat = {
    "rho": 7.85,
    "E": 210000,
    "nu": 0.3
}

# del solid_mat   #删除整个字典
print(solid_mat)

del solid_mat["rho"]
print(solid_mat)    # {'E': 210000, 'nu': 0.3}

solid_mat.clear()
print(solid_mat)    # {}



solid_mat2 = {
    "rho": 2.7,
    "E": 72000,
    "nu": 0.33
}

solid_mat2.pop("E")
print(solid_mat2)   # {'rho': 2.7, 'nu': 0.33}

solid_mat2.popitem()
print(solid_mat2)   # {'rho': 2.7}，PYTHON 3.7之后，popitem默认删除最后一个键值对


# -------------------------------------------------------------

"""
常见操作
len()：求长度
keys：返回所有键名
"""

dic3 = {
    "rho": 1.1,
    "E": 17000,
    "nu": 0.45
}

print(len(dic3))    # 3

print(dic3.keys())  # dict_keys(['rho', 'E', 'nu'])
print(type(dic3.keys()))    # <class 'dict_keys'> ，特殊类型


"""取值用for循环取值"""
list1 = [i for i in dic3.keys()]
print(list1)    # ['rho', 'E', 'nu']

list2 = [i for i in dic3.values()]
print(list2)    # [1.1, 17000, 0.45]


"""取键值对，items()，返回的类型为tuple"""
for i in dic3.items():
    print(i)