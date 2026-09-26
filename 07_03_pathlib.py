from pathlib import Path

path = Path("docs_pathlib_temp/test.txt")
path_dir = Path("docs_pathlib_temp")

"""
完整名称 -> str
"""
print(path.name)    # test.txt


"""
文件名，不含扩展名 -> str
"""
print(path.stem)    # test


"""
扩展名 -> str
"""
print(path.suffix)  # .txt


"""
父路径 -> Path
"""
print(path.parent)  # docs_pathlib_temp


"""
路径拼接 -> Path
"""
root = Path(r"E:\study_code")
file = root / "study_python" / "docs_pathlib_temp" / "test.txt"


"""
当前工作目录 -> Path
"""
print(Path.cwd())     # E:\study_code\study_python


"""
当前用户家目录 -> Path
"""
print(Path.home())  # C:\Users\ying


"""
__file__ 表示当前Python文件自己的路径 -> Path
"""
print(Path(__file__))   # e:\study_code\study_python\07_03_pathlib.py
print(Path(__file__).parent)    # e:\study_code\study_python，得到当前Python文件的文件夹路径


"""
路径是否存在 -> bool
"""
print(path.exists())    # True


"""
是否是文件 -> bool
"""
print(path.is_file())   # True


"""
是否是文件夹 -> bool
"""
print(path.is_dir())    # False


"""
创建文件夹 -> None
"""
new_dir = Path(r"E:\study_code\hahaha")
# new_dir.mkdir()     # 父路径不存在或已存在文件夹会报错
# new_dir.mkdir(parents=True, exist_ok=True)  # 工程经常这样写，自动创建父目录，文件夹存在也不报错


"""
遍历文件夹 -> Iterator[Path]
"""
result = path_dir.iterdir()     # 返回可迭代对象
for path_result in result:
    print(path_result)     # docs_pathlib_temp\1.k    3.k  test.txt


"""
按规则寻找文件 -> Iterator[Path]
"""
for file in path_dir.glob("*.k"):
    print(file)     # docs_pathlib_temp\1.k     3.k


"""
递归搜索 -> Iterator[Path]
"""
for file in path_dir.rglob("*.k"):
    print(file)     # docs_pathlib_temp\1.k     3.k


"""
读文件 -> str
"""
text = path.read_text(encoding="utf-8")
print(text)     # 3.1    8979  2643  哈哈哈


"""
写文件 -> int (写入的字符数)    注意，注意，注意：会覆盖掉原来的字符
"""
result = path.write_text(
    "hello_python",
    encoding="utf-8"
)
print(result)   # 12


"""
读二进制文件 -> bytes
"""
data = path.read_bytes()
print(data)     # b'hello_python'


"""
写二进制文件 -> int (写入的字节数)    注意，注意，注意：会覆盖掉原来的字节
"""
# result = path.write_bytes(bytes(152))   # bytes(152)，表示创建一个长度为 152 的 bytes 对象，并且里面所有字节都是 0
# print(result)

"""
str  --encode()--> bytes
bytes --decode()--> str
"""

# --------------------------


"""---文件操作---"""

"""
重命名 -> Path      若重命名后的文件本身就存在，则报错
"""
print("***rename***")
path2 = Path("docs_pathlib_temp/test102.txt")
# path2.rename("docs_pathlib_temp/test103.txt")    # Windows 下，目标文件 test102.txt 已存在时通常会报错
# print(path2)    # docs_pathlib_temp\test102.txt，指向的仍然是test102.txt



"""
替换/移动 -> Path   若重命名后的文件本身就存在，则删除存在的文件后，用当前文件替换
"""
print("***replace***")
path3 = path2.replace("docs_pathlib_temp/test103.txt")  # 即使目标已经存在，也用当前文件替换它，但要求当前文件存在

print(path2)    # docs_pathlib_temp\test102.txt
print(path3)    # docs_pathlib_temp\test103.txt

"""
path2
  ↓
Path("docs_pathlib_temp/test102.txt")

replace(...)
  ↓
磁盘上的 test102.txt 被改成 test103.txt
  ↓
但是 path2 这个 Path 对象本身没有改变

关键原因是：Path 对象是不可变的
"""



"""
删除 -> None
"""
path3.unlink()   # 主要用于文件，不是普通文件夹


"""
获取规范化绝对路径 -> Path
"""
print("***resolve***")
print(path.resolve())   # E:\study_code\study_python\docs_pathlib_temp\test.txt




"""
pathlib
   │
   └── Path
        │
        ├── 路径信息
        │     ├── .name
        │     ├── .stem
        │     ├── .suffix
        │     └── .parent
        │
        ├── 路径创建/拼接
        │     ├── Path(...)
        │     ├── Path.cwd()
        │     ├── Path.home()
        │     └── /
        │
        ├── 判断
        │     ├── .exists()
        │     ├── .is_file()
        │     ├── .is_dir()
        │     └── .is_absolute()
        │
        ├── 查找/遍历
        │     ├── .iterdir()
        │     ├── .glob()
        │     └── .rglob()
        │
        ├── 文件夹
        │     └── .mkdir()
        │
        ├── 文件读写
        │     ├── .read_text()
        │     ├── .write_text()
        │     ├── .read_bytes()
        │     └── .write_bytes()
        │
        └── 文件操作
              ├── .rename()
              ├── .replace()
              └── .unlink()
"""