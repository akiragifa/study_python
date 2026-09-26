"""
匿名函数

    函数名 = lambda 形参: 返回值(表达式)


"""

def add1(a, b):
    return a + b

result = add1(1, 3)
print(result)   # 4



"""使用匿名函数实现上述功能"""

add2 = lambda a, b: a + b

result2 = add2(1, 3)
print(result2)  # 4




"""lambda的无参数形式"""

print_name = lambda: "akiragifa"

print(print_name())     # akiragifa




"""lambda的单参数形式"""

nums = lambda num: num

print(nums(3))   # 3



"""lambda的默认参数形式"""

func = lambda name, age = 18: (name, age)

print(func("akiragifa"))    # ('akiragifa', 18)
print(func("xixi", 20))     # ('xixi', 20)



"""lambda的关键字参数形式"""

func2 = lambda name, age: (name, age)
print(func2(age = 18, name = "haha"))   # ('haha', 18)


func3 = lambda **kwargs: kwargs
print(func3(section = "shell", thickness = 1.0))    # {'section': 'shell', 'thickness': 1.0}


# -------------------------------------------------------------
# -------------------------------------------------------------



"""
虽然你可以写：add = lambda a, b: a + b
但通常不推荐，因为：
    def add(a, b):
        return a + b
更清除

lambda 真正适合的是：函数只临时使用一次，不值得专门写一个 def。最经典的场景就是 sort()


"""

students = [
    ["akira", 90],
    ["xingxing", 75],
    ["yingying", 88]
]

students.sort(key = lambda x: x[1])     # 按照成绩排序
print(students)     # [['xingxing', 75], ['yingying', 88], ['akira', 90]]



numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))     # [2, 4, 6, 8]



numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))     # [2, 4, 6]



# -------------------------------------------------------------

"""lambda中写条件表达式"""

judge = lambda age: "成年" if age >= 18 else "未成年"

print(judge(1))     # 未成年
print(judge(20))    # 成年