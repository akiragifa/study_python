"""
知识体系：

Python 标准库
│
├── pathlib      ← 文件路径
├── os           ← 操作系统相关操作
├── shutil       ← 文件复制、移动、删除目录
├── json         ← JSON 数据
├── csv          ← CSV 文件
├── re           ← 正则表达式
└── ...

"""


"""
Path
│
├─【常用实例属性 / property】
│
├─ .name ─────────────────────→ 文件/目录名
│                               → str
│
├─ .stem ─────────────────────→ 不带最后一个扩展名的文件名
│                               → str
│
├─ .suffix ───────────────────→ 最后一个扩展名
│                               → str
│
├─ .suffixes ─────────────────→ 所有扩展名组成的列表
│                               → list[str]
│
├─ .parent ───────────────────→ 父路径
│                               → Path
│
├─ .parents ──────────────────→ 所有祖先路径
│                               → Sequence[Path]
│
├─ .parts ────────────────────→ 路径各组成部分
│                               → tuple[str, ...]
│
├─ .anchor ───────────────────→ 路径锚点
│                               → str
│
├─ .drive ────────────────────→ Windows 盘符
│                               → str
│
├─ .root ─────────────────────→ 根路径
│                               → str
│
│
├─【常用实例方法】
│
├─ .exists() ─────────────────→ 路径是否存在
│                               → bool
│
├─ .is_file() ────────────────→ 是否是普通文件
│                               → bool
│
├─ .is_dir() ─────────────────→ 是否是目录
│                               → bool
│
├─ .is_symlink() ─────────────→ 是否是符号链接
│                               → bool
│
├─ .is_absolute() ────────────→ 是否为绝对路径
│                               → bool
│
├─ .absolute() ───────────────→ 得到绝对路径形式
│                               → Path
│
├─ .resolve() ────────────────→ 解析为规范化绝对路径
│                               → Path
│
├─ .read_text() ──────────────→ 读取全部文本内容
│                               → str
│
├─ .read_bytes() ─────────────→ 读取全部二进制内容
│                               → bytes
│
├─ .write_text() ─────────────→ 写入文本
│                               → int
│                                 （写入的字符数）
│
├─ .write_bytes() ────────────→ 写入二进制数据
│                               → int
│                                 （写入的字节数）
│
├─ .open() ───────────────────→ 打开文件
│                               → TextIO / BinaryIO
│                                 （文件对象）
│
├─ .iterdir() ────────────────→ 遍历当前目录中的内容
│                               → Iterator[Path]
│
├─ .glob() ───────────────────→ 按模式匹配当前路径下的内容
│                               → Iterator[Path]
│
├─ .rglob() ──────────────────→ 递归进行模式匹配
│                               → Iterator[Path]
│
├─ .mkdir() ──────────────────→ 创建目录
│                               → None
│
├─ .touch() ──────────────────→ 创建文件或更新时间
│                               → None
│
├─ .unlink() ─────────────────→ 删除文件/符号链接
│                               → None
│
├─ .rmdir() ──────────────────→ 删除空目录
│                               → None
│
├─ .rename() ─────────────────→ 重命名/移动
│                               → Path
│
├─ .replace() ────────────────→ 替换目标文件并移动
│                               → Path
│
├─ .with_name() ──────────────→ 替换文件名
│                               → Path
│
├─ .with_stem() ──────────────→ 替换 stem
│                               → Path
│
├─ .with_suffix() ────────────→ 替换扩展名
│                               → Path
│
├─ .joinpath() ───────────────→ 拼接路径
│                               → Path
│
├─ .relative_to() ────────────→ 得到相对某路径的相对路径
│                               → Path
│
├─ .samefile() ───────────────→ 两个路径是否指向同一文件
│                               → bool
│
├─ .stat() ───────────────────→ 获取文件系统状态信息
│                               → os.stat_result
│
│
├─【常用类方法】
│
├─ Path.cwd() ────────────────→ 当前工作目录
│                               → Path
│
└─ Path.home() ───────────────→ 当前用户的主目录
                                → Path


"""

"""
分类记忆：

Path
│
├─ 路径的信息
│   ├─ name → str
│   ├─ suffix → str
│   └─ parent → Path
│
├─ 判断路径
│   ├─ exists() → bool
│   ├─ is_file() → bool
│   └─ is_dir() → bool
│
├─ 读取/写入
│   ├─ read_text() → str
│   ├─ read_bytes() → bytes
│   ├─ write_text() → int
│   └─ write_bytes() → int
│
├─ 查找/遍历
│   ├─ iterdir() → Iterator[Path]
│   ├─ glob() → Iterator[Path]
│   └─ rglob() → Iterator[Path]
│
├─ 修改文件系统
│   ├─ mkdir() → None
│   ├─ touch() → None
│   ├─ unlink() → None
│   └─ rmdir() → None
│
├─ 生成新路径
│   ├─ resolve() → Path
│   ├─ joinpath() → Path
│   ├─ with_name() → Path
│   └─ with_suffix() → Path
│
└─ 类级操作
    ├─ Path.cwd() → Path
    └─ Path.home() → Path


"""

"""
常用：

Path
│
├─【属性】
│
├─ .name ──────────────→ 文件名
│                        → str
│
├─ .stem ──────────────→ 不含扩展名的文件名
│                        → str
│
├─ .suffix ────────────→ 扩展名
│                        → str
│
├─ .parent ────────────→ 父路径
│                        → Path
│
│
├─【判断】
│
├─ .exists() ──────────→ 是否存在
│                        → bool
│
├─ .is_file() ─────────→ 是否是文件
│                        → bool
│
├─ .is_dir() ──────────→ 是否是目录
│                        → bool
│
│
├─【读取 / 写入】
│
├─ .read_text() ───────→ 文本内容
│                        → str
│
├─ .read_bytes() ──────→ 二进制内容
│                        → bytes
│
├─ .write_text() ──────→ 写入的字符数
│                        → int
│
├─ .write_bytes() ─────→ 写入的字节数
│                        → int
│
│
├─【目录操作】
│
├─ .iterdir() ─────────→ 当前目录内容
│                        → Iterator[Path]
│
├─ .glob() ────────────→ 匹配到的路径
│                        → Iterator[Path]
│
├─ .rglob() ───────────→ 递归匹配到的路径
│                        → Iterator[Path]
│
├─ .mkdir() ───────────→ 创建目录
│                        → None
│
│
├─【路径处理】
│
├─ .resolve() ─────────→ 解析后的绝对路径
│                        → Path
│
├─ .with_name() ───────→ 修改文件名后的路径
│                        → Path
│
├─ .with_suffix() ─────→ 修改扩展名后的路径
│                        → Path
│
├─ .joinpath() ────────→ 拼接后的路径
│                        → Path
│
│
└─【类方法】
   │
   ├─ Path.cwd() ──────→ 当前工作目录
   │                    → Path
   │
   └─ Path.home() ─────→ 用户主目录
                        → Path

"""