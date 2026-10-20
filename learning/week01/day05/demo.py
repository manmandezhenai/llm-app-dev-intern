"""
Week01-Day05 模块、包与异常处理示例代码
包含：模块导入、异常处理、自定义异常标准化示例 + 文件读取工具综合练习
"""
import os
import json

# ---------------------- 第一部分：知识点标准化示例 ----------------------
# 1. 基础异常捕获
print("=== 1. 基础异常捕获演示 ===")


def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为0")
        return None


print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# 2. 多异常捕获 + else + finally
print("\n=== 2. 完整异常结构演示 ===")


def read_number(filename):
    try:
        file = open(filename, "r", encoding="utf-8")
        content = file.read()
        num = int(content)
    except FileNotFoundError:
        print("异常：文件不存在")
        return None
    except ValueError:
        print("异常：文件内容不是有效整数")
        return None
    else:
        print("文件读取成功，无异常")
        return num
    finally:
        # 无论是否异常都关闭文件
        try:
            file.close()
            print("文件资源已释放")
        except NameError:
            pass


# 测试用例：文件不存在场景
read_number("not_exist.txt")

# 3. 主动抛出异常
print("\n=== 3. 主动抛出异常演示 ===")


def check_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")

    if age < 0 or age > 150:
        raise ValueError("年龄范围必须在0-150之间")

    print(f"年龄校验通过：{age}")


try:
    check_age(200)
except ValueError as e:
    print(f"捕获到值错误：{e}")

# 4. 自定义异常
print("\n=== 4. 自定义异常演示 ===")


class BusinessError(Exception):
    """业务逻辑异常基类"""

    def __init__(self, message, code=1000):
        super().__init__(message)
        self.code = code


def withdraw(balance, amount):
    if amount > balance:
        raise BusinessError("余额不足", code=2001)

    return balance - amount


try:
    withdraw(100, 200)
except BusinessError as e:
    print(f"业务异常：[错误码{e.code}]")


# ---------------------- 第二部分：综合实操小练习 ----------------------
def config_reader_tool():
    """
    综合练习：配置文件读取工具
    功能：读取JSON配置文件，支持异常处理、参数校验、默认值返回
    技术点：异常处理、自定义异常、文件操作、字典操作
    """
    print("\n=== 综合小练习：配置文件读取工具 ===")

    class ConfigParseError(Exception):
        """配置解析异常"""
        pass

    def load_config(config_file, default_config=None):
        """
        加载JSON配置文件
        :param config_file: 配置文件路径
        :param default_config: 默认配置，加载失败时返回
        :return:
        """
        if default_config is None:
            default_config = {}
        try:
            if not os.path.exists(config_file):
                raise FileNotFoundError(f"配置文件{config_file}不存在")

            with open(config_file, "r", encoding="utf-8") as f:
                try:
                    config = json.load(f)
                except json.decoder.JSONDecodeError:
                    raise ConfigParseError("配置文件格式不是合法JSON")

            if not isinstance(config, dict):
                raise ConfigParseError("配置文件根节点必须是字典")

            return config
        except FileNotFoundError as e:
            print(f"[警告] {e}，使用默认配置")
            return default_config
        except ConfigParseError as e:
            print(f"[错误] {e}，使用默认配置")
            return default_config

    # 测试1：创建测试配置文件
    test_config = {
        "app_name": "AI应用",
        "version": "1.0.0",
        "port": 8000,
        "debug": True
    }

    with open("test_config.json", "w", encoding="utf-8") as f:
        json.dump(test_config, f, ensure_ascii=False, indent=2)

    # 测试正常读取
    config = load_config("test_config.json")
    print(f"加载成功，配置内容：{config}")

    # 测试文件不存在
    config2 = load_config("no_config.json", default_config={"app_name": "默认应用"})
    print(f"加载失败返回默认配置：{config2}")

    # 清理测试文件
    if os.path.exists("test_config.json"):
        os.remove("test_config.json")


if __name__ == "__main__":
    config = config_reader_tool()
