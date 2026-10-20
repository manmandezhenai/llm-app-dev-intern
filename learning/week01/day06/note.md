# Week01-Day06：文件操作与内置库（os / datetime / json）

## 【核心知识点】

### 1. 文件操作基础

- 打开函数：`open(文件路径, 模式, encoding)`，返回文件对象，操作完成必须关闭
- 常用打开模式：

| 模式          | 说明        | 注意事项                   |
|-------------|-----------|------------------------|
| `r`         | 只读模式（默认值） | 文件不存在会报错               |
| `w`         | 只写模式      | 文件不存在则创建，存在则**清空原有内容** |
| `a`         | 追加模式      | 文件不存在则创建，存在则在末尾追加内容    |
| `rb` / `wb` | 二进制读写模式   | 用于图片、视频、压缩包等非文本文件      |

- 读写方法：
    - 读：`read()` 读取全部内容、`readline()` 读取一行、`readlines()` 读取所有行返回列表
    - 写：`write(字符串)` 写入字符串、`writelines(字符串列表)` 批量写入
- 上下文管理器：`with open(...) as f:`，代码块执行完毕自动关闭文件，工程代码强制使用
- 编码规范：文本文件统一指定 `encoding="utf-8"`，避免平台乱码

### 2. os 系统模块

- 路径处理（os.path 子模块）：
    - `os.path.exists(path)`：判断路径是否存在
    - `os.path.isfile(path)`：判断是否为文件
    - `os.path.isdir(path)`：判断是否为目录
    - `os.path.join(path1, path2)`：拼接路径，自动适配系统分隔符，工程代码强制使用
    - `os.path.abspath(path)`：获取绝对路径
- 目录与文件操作：
    - `os.mkdir(dir)`：创建单级目录
    - `os.makedirs(dir, exist_ok=True)`：创建多级目录，目录已存在不报错
    - `os.listdir(dir)`：列出目录下所有文件与子目录名
    - `os.remove(file)`：删除指定文件
    - `os.rmdir(dir)`：删除空目录
- 其他常用：`os.getcwd()` 获取当前工作目录、`os.rename(old, new)` 重命名文件

### 3. datetime 时间模块

- 核心类：`datetime.datetime`，表示具体的日期时间点
- 时间获取：`datetime.datetime.now()` 获取当前本地时间
- 时间格式化：
    - `strftime(格式字符串)`：时间对象转格式化字符串
    - 常用格式符：`%Y` 四位年、`%m` 两位月、`%d` 两位日、`%H` 24 小时制、`%M` 分钟、`%S` 秒
- 时间解析：`datetime.datetime.strptime(字符串, 格式)`：字符串转时间对象
- 时间差：`datetime.timedelta(days=0, hours=0, minutes=0)`，用于时间加减运算
- 时间戳：`时间对象.timestamp()` 转时间戳，`datetime.fromtimestamp(戳)` 时间戳转时间对象

### 4. json 模块序列化模块

- 核心概念：序列化是 Python 对象转 JSON 字符串，反序列化是 JSON 字符串转 Python 对象
- 常用方法：
    - `json.dumps(obj)`：Python 对象转 JSON 字符串
    - `json.loads(str)`：JSON 字符串转 Python 对象
    - `json.dump(obj, 文件对象)`：直接序列化写入文件
    - `json.load(文件对象)`：直接从文件读取反序列化
- 关键参数：
    - `ensure_ascii=False`：保留中文，不转义为 Unicode 编码，中文场景必须加
    - `indent=2`：格式化缩进，提升可读性，配置文件推荐使用
- 类型对应：JSON 仅支持字符串、数字、布尔、数组、对象、null，对应 Python 的 `str / int / float / bool / list / dict / None`

## 【今日易错点】

1. 文件打开后忘记关闭会导致资源泄露，工程代码必须使用 `with` 上下文管理器自动释放
2. `w` 模式打开已存在的文件会直接清空全部原有内容，写入前务必确认模式正确
3. 手动用字符串加号拼接路径会导致跨平台兼容问题，必须使用 `os.path.join` 拼接
4. `json` 序列化中文默认会转义成 Unicode 编码，需要设置 `ensure_ascii=False` 保留中文
5. `datetime` 格式化月份是 `%m`、分钟是 `%M`，大小写混淆会导致格式化结构错误
6. `readlines` 返回的列表每行末尾自带换行符，使用前需要用 `strip()` 去除空白字符
7. `os.remove` 只能删除文件，删除目录要用 `os.rmdir` 且目标目录必须为空
8. `json` 只能序列化 Python 内置基础数据，自定义类对象无法直接序列化