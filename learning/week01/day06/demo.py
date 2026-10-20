"""
Week01-Day06 文件操作与内置库示例代码
包含：文件读写、os模块、datetime、json标准化示例 + 用户数据持久化管理综合练习
"""

import os
import json
from datetime import datetime, timedelta

# ---------------------- 第一部分：知识点标准化示例 ----------------------
# 1. 文件读写
print("=== 1. 文件读写演示 ===")
test_file = "demo_test.txt"
# 写入文件
with open(test_file, "w", encoding="utf-8") as f:
    f.write("第一行内容\n")
    f.write("第二行内容\n")
    lines = ["第三行", "第四行", "第五行"]
    f.writelines([line + "\n" for line in lines])
print("文件写入完成")

# 读取文件
with open(test_file, "r", encoding="utf-8") as f:
    content = f.read()
    print("\n文件全部内容：")
    print(content)

# 按行读取
with open(test_file, "r", encoding="utf-8") as f:
    print("\n按行读取：")
    for index, line in enumerate(f, 1):
        print(f"    行{index}：{line.strip()}")

# 清理测试文件
os.remove(test_file)

# 2. os 模块
print("\n=== 2. os模块演示 ===")
# 路径操作
current_dir = os.getcwd()
print(f"当前工作目录：{current_dir}")

test_dir = "test_dir"
sub_dir = os.path.join(test_dir, "sub")
os.makedirs(sub_dir, exist_ok=True)
print(f"创建多级目录：{sub_dir}")

print(f"目录是否存在：{os.path.exists(test_dir)}")
print(f"是否为目录：{os.path.isdir(test_dir)}")

# 清理测试目录
os.rmdir(sub_dir)
os.rmdir(test_dir)

# 3. datetime
print("\n=== 3. datetime时间演示 ===")
now = datetime.now()
print(f"当前时间：{now}")

# 格式化输出
format_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"格式化时间：{format_str}")

# 字符串转时间
time_str = "2024-01-01 12:00:00"
parse_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print(f"解析时间：{parse_time}")

# 时间差计算
after_7_days = now + timedelta(days=7)
print(f"7天后的时间：{after_7_days.strftime('%Y-%m-%d')}")

# 4. json 序列化
print("\n=== 4. json序列化演示 ===")
user_data = {
    "name": "张三",
    "age": 22,
    "hobbies": ["编程", "阅读"],
    "is_student": True,
    "address": None
}

# 转JSON字符串
json_str = json.dumps(user_data, ensure_ascii=False, indent=2)
print("\nJSON字符串：")
print(json_str)

# JSON转Python对象
py_obj = json.loads(json_str)
print(f"\n反序列化后类型：{type(py_obj)}，姓名：{py_obj['name']}")


# ---------------------- 第二部分：综合实操小练习 ----------------------
def user_data_persistence():
    """
    综合练习：用户数据持久化管理系统
    功能：用户注册、查询、列表展示，数据通过json文件持久化存储
    技术点：文件操作、os模块、json、datetime、字典列表操作
    """
    print("\n=== 综合小练习：用户数据持久化管理系统 ===")
    date_file = "users.json"

    def load_users():
        """加载用户数据，文件不存在则返回空列表"""
        if not os.path.exists(date_file):
            return []
        with open(date_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_users(users):
        """保存用户数据到文件"""
        with open(date_file, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def add_user(name, age):
        """添加新用户"""
        users = load_users()
        user = {
            "name": name,
            "age": age,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        users.append(user)
        save_users(users)
        print(f"用户【{name}】添加成功！")

    def list_users():
        """列出所有用户"""
        users = load_users()
        if not users:
            print("暂无用户数据！")
            return
        print("\n用户列表：")
        for index, user in enumerate(users, 1):
            print(f"    {index}. {user['name']} - {user['age']} - {user['create_time']}")

    # 测试功能
    add_user("张三", 22)
    add_user("李四", 21)
    add_user("王五", 23)
    list_users()

    # 清空测试文件
    if os.path.exists(date_file):
        os.remove(date_file)


if __name__ == "__main__":
    user_data_persistence()
