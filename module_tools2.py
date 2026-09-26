def greet(name):
    return f"Hello, {name}"

print("顶层")   # 导入时这行代码也会执行

name = "akiragifa"

def add(a, b):
    return a + b


"""
被调用时不会执行，只有执行此函数文件时，才会执行

经常用于：把模块的正式功能和测试/演示代码分开
"""
if __name__ == "__main__":
    print("Hi")
    x = 10
    print(x)
