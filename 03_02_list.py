"""
[xxx, "aa"] 表示列表

列表中的元素类型可以不相同

"""

li = [1, 2, 3, 4]
print(li)   # [1, 2, 3, 4]
print(type(li))     # <class 'list'>

print(li[0])    # 1

for i in li:
    print(i)    # 遍历列表

# -------------------------------------------------------------

"""
列表的相关操作

"""

"""
append：1次添加1个
extend：可迭代对象一个个取出来添加
insert：插入
"""
li2 = [1, 2, "xixi", "haha"]
li2.append("akiragifa")     
print(li2)      # [1, 2, 'xixi', 'haha', 'akiragifa']

li3 = [1, 2, "xixi", "haha"]
li3.extend("xingxing")  # [1, 2, 'xixi', 'haha', 'x', 'i', 'n', 'g', 'x', 'i', 'n', 'g']
print(li3)

li4 = [1, 2, "xixi", "haha"]
li4.insert(0, "akiragifa")
print(li4)      # ['akiragifa', 1, 2, 'xixi', 'haha']


# -------------------------------------------------------------

"""
修改：通过下标
"""
li5 = [1, 2, "xixi", "haha"]
li5[1] = "akiragifa"
print(li5)      # [1, 'akiragifa', 'xixi', 'haha']


# -------------------------------------------------------------

"""
查询：与字符串类似
in 
not in
index
count
"""
li6 = [1, 2, "xixi", "haha"]
print(1 in li6)     # True
print(1 not in li6)     # False
print(li6.index(2))     # 1
print(li6.count("a"))   # 0


"""
用户输入昵称，昵称重复则不能使用
"""
used_name = ["xingxing", "yingying", "akiragifa"]
name = input("请输入名称：")
if(name in used_name):
    print("名称重复，无法使用")
else:
    print("注册成功")


# -------------------------------------------------------------

"""
删除：
del
pop：根据索引删除，默认删除最后一个
remove：根据值进行删除
"""
li7 = ["xingxing", "yingying", "akiragifa"]
# del li7     # 直接将li7删除
print(li7)

del li7[2]
print(li7)      # ['xingxing', 'yingying']


li8 = ["xingxing", "yingying", "akiragifa"]
li8.pop()
print(li8)  # ['xingxing', 'yingying']，默认删除最后一个

li8.pop(0)
print(li8)  # ['yingying']，指定索引进行删除


li9 = ["xingxing", "yingying", "akiragifa"]
li9.remove("xingxing")
print(li9)      # ['yingying', 'akiragifa']，如果有重复，默认删除第一次出现的


# -------------------------------------------------------------

"""
排序：
sort：从小到大排序
reverse：反写字符串
"""
li10 = [3, 6, 23, 564, 4, 5, 90]
li10.sort()
print(li10)     # [3, 4, 5, 6, 23, 90, 564]


li11 = [3, 6, 23, 564, 4, 5, 90]
li11.reverse()
print(li11)     # [90, 5, 4, 564, 23, 6, 3]


li12 = [3, 6, 23, 564, 4, 5, 90]
li12.sort(reverse=True)     # [90, 5, 4, 564, 23, 6, 3]，先排序再倒序


# -------------------------------------------------------------

"""
列表推导式
"""

li13 = []
for i in range(1, 6):
    li13.append(i)
print(li13)     # [1, 2, 3, 4, 5]


"""更简便的写法为"""

li14 = [i for i in range(1, 6)]
print(li14)     # [1, 2, 3, 4, 5]


li15 = [i for i in range(1, 11) if i % 2 == 0]
print(li15)     # [2, 4, 6, 8, 10]


# -------------------------------------------------------------

"""
列表嵌套
"""

li16 = [1, 2, 3, [4, 5, 6]]
print(li16[3])  # [4, 5, 6]
print(li16[3][0])   # 4