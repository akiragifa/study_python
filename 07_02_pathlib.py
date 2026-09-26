from pathlib import Path, WindowsPath
from sys import path_hooks

p0 = Path("docs_pathlib_temp/test.txt")   # 创建Path类的对象，相对路径
p1 = Path("test.txt")  # 当前目录下直接寻找文件
p2 = Path(r"E:\study_code\study_python\docs_pathlib_temp\test.txt") # 绝对路径的第一种写法
p3 = Path("E:/study_code/study_python/docs_pathlib_temp/test.txt")  # 绝对路径的第一种写法

# BASE_DIR = Path(__file__).resolve().parent    相对路径的写法

# =============================================================
"""
├─ Path.cwd() ────────────────→ 类方法，返回当前工作目录
│                               → Path的实例对象
"""

path = Path.cwd()
print(path)     # E:\study\study_python
print(type(path))   # <class 'pathlib.WindowsPath'>
print(isinstance(path, Path))   # True
print(isinstance(path, WindowsPath))    # True，WindowsPath是Path的子类
print(issubclass(WindowsPath, Path))    # True，WindowsPath是Path的子类


# -------------------------------------------------------------

"""
└─ Path.home() ───────────────→ 类方法，当前用户的主目录
                                → Path的实例对象
"""
path2 = Path.home()
print(path2)    # C:\Users\ying
print(type(path2))  # <class 'pathlib.WindowsPath'>

path3 = Path.home() / "Desktop"
print(path3)    # C:\Users\ying\Desktop


# =============================================================

"""
/  拼接路径
"""

root = Path("E:/study_code")
file = root / "study_python" / "docs_pathlib_temp" / "test.txt"
print(file)     # E:\study_code\study_python\docs_pathlib_temp\test.txt
print(type(file))   # <class 'pathlib._local.WindowsPath'>


# =============================================================


"""
├─ .name ─────────────────────→ 属性，文件/目录名
│                               → str

├─ .stem ─────────────────────→ 属性，不带最后一个扩展名的文件名
│                               → str

├─ .suffix ───────────────────→ 属性，最后一个扩展名
│                               → str

├─ .parent ───────────────────→ 属性，父路径
│                               → Path
"""

file4 = Path(r"E:\study_code\study_python\docs_pathlib_temp\test.txt")
print(file4.name)   # test.txt
print(file4.stem)   # test
print(file4.suffix)     # .txt

print(file4.parent)     # E:\study\study_python\docs_pathlib_temp
print(type(file4.parent))   # <class 'pathlib.WindowsPath'>

print(file4.parent.parent)  # E:\study\study_python


path4 = Path(r"E:\study_code\study_python\docs_pathlib_temp")
print(path4.name)   # docs_pathlib_temp
print(path4.parent)     # E:\study\study_python


# =============================================================
"""
├─ .exists() ─────────────────→ 实例方法，路径是否存在
│                               → bool
"""

file5 = Path(r"E:\study_code\study_python\docs_pathlib_temp\test.txt")

if file5.exists():
    print("存在")   # 存在
else:
    print("不存在")


# -------------------------------------------------------------
"""
├─ .is_file() ────────────────→ 是否是普通文件
│                               → bool

├─ .is_dir() ─────────────────→ 是否是目录
│                               → bool
"""

file6 = Path(r"E:\study_code\study_python\docs_pathlib_temp\test.txt")
path6 = Path(r"E:\study_code\study_python\docs_pathlib_temp")

print(file6.is_file())  # True
print(file6.is_dir())   # False

print(path6.is_file())  # False
print(path6.is_dir())   # True


# -------------------------------------------------------------
"""
├─ .mkdir() ──────────────────→ 实例方法，创建文件夹
│                               → None
"""

folder = Path("test_folder")

# folder.mkdir()  # 在当前目录下，创建名称为 "test.folder" 的文件夹
# folder.mkdir()  # 若当前目录下已有要创建的文件夹，则报错
folder.mkdir(exist_ok=True)     # 就算已有此文件，也不报错



# Path("test/test_folder2").mkdir()   # 报错，找不到父路径
Path("test/test_folder2").mkdir(parents=True, exist_ok=True)   # 更稳妥的写法，连同父路径一起创建


# -------------------------------------------------------------
"""
├─ .iterdir() ────────────────→ 实例方法，遍历当前目录中的内容，只遍历一层
│                               → Iterator[Path]
"""

path7 = Path(r"E:\study_code\study_python")
li = path7.iterdir()

print(li)   # <generator object Path.iterdir at 0x000001E4E28AF780>，li不是列表，而是目录迭代器对象，打印的是目录迭代器对象的地址
print(type(li))     # <class 'generator'>
# print(list(li))   # [WindowsPath('E:/study/study_python/.git'), ...]，将迭代器里面的内容取出，组成一个列表


for item in path7.iterdir():
    print(item)
    print(type(item))   # <class 'pathlib.WindowsPath'>


# -------------------------------------------------------------
"""
├─ .glob() ───────────────────→ 按模式匹配当前路径下的内容，只找当前层级
│                               → Iterator[Path]

├─ .rglob() ──────────────────→ 递归进行模式匹配，找当前层级 + 所有子目录
│                               → Iterator[Path]
"""

print("\n")

folder2 = Path(r"E:\study_code\study_python")

for file in folder2.glob("*.txt"):
    print(file)     # 找当前目录下的所有.txt文件

print("\n")

for file in folder2.rglob("*.txt"):
    print(file)     # 递归朝找当前目录及所有子目录下的.txt文件






"""
p.read_text()
p.write_text()
p.resolve()
p.relative_to()
p.rename()
p.unlink()

"""
# text1 = path.read_text()    # 不推荐，尽量写清楚编码规则
text1 = p0.read_text(encoding="utf-8")
print(text1)
print(type(text1))  # <class 'str'>

print(p0.exists())    # True
print(p1.exists())   # False
print(p2.exists())   # True
print(p3.exists())   # True

Path.cwd