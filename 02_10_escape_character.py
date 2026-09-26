"""
转义字符:

\ 称为转义字符（escape character）
\n 称为转义序列（escape sequence）


| 转义序列 | 作用 | 示例 |
|---|---|---|
| `\n` | 换行 | `"Hello\nWorld"` |
| `\t` | 水平制表符（Tab） | `"姓名\t年龄"` |
| `\\` | 表示一个反斜杠 | `"C:\\Users\\ying"` |
| `\'` | 表示单引号 | `'It\'s Python'` |
| `\"` | 表示双引号 | `"他说：\"你好\""` |
| `\r` | 回车，将光标移到当前行开头 | `"Hello\rHi"` |
| `\b` | 退格 | `"abc\b"` |
| `\a` | 响铃字符 | `"\a"` |
| `\f` | 换页符 | `"第一页\f第二页"` |
| `\v` | 垂直制表符 | `"上面\v下面"` |
"""

print("我是akiragifa\n我30岁")
print("我是akiragifa\t我30岁")
print("Hello\rHi")  # Hillo，Hi移动到了本行开头，替代了He
print("abc\bX")     # abX，光标移动到c前，X取代c的位置
print("abc\b\na")   # \b光标在c前，\n光标在下一行，再输出a

print(r"D:\Game_tools")     # D:\Game_tools，前面加r表示"\"不进行转义