"""
Week01-Day01 Python基础语法示例代码
包含：变量、数据类型、输入输出、注释规范的标准化示例 + 综合实操练习
"""

# ---------------------- 第一部分：知识点标准化示例 ----------------------
# 1. 变量定义与数据类型
user_name = "张三"
user_age = 22
user_height = 1.78
is_student = True

print("=== 1. 数据类型演示 ===")
print(f"user_name 类型：{type(user_name)}，值：{user_name}")
print(f"user_age 类型：{type(user_age)}，值：{user_age}")
print(f"user_height 类型：{type(user_height)}，值：{user_height}")
print(f"is_student 类型：{type(is_student)}，值：{is_student}")

# 2. 类型转换
print("\n=== 2. 类型转换演示 ===")
age_str = "25"
age_int = int(age_str)
print(f"字符串转整数：{repr(age_str)} → {age_int}，类型：{type(age_int)}")

score = 95
score_str = str(score)
print(f"整数转字符串：{score} → {repr(score_str)}，类型：{type(score_str)}")

# 3. 输入与输出
print("\n=== 3. 输入与输出演示 ===")
# 计算两数之和
num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
print(f"两数之和：{num1 + num2}")


# ---------------------- 第二部分：综合实操小练习 ----------------------
def user_info_collect():
    """
    综合练习：用户信息录入小程序
    功能：接收用户输入的姓名、年龄、身高，输出格式化的个人信息卡片
    """
    print("\n=== 综合小练习：用户信息录入系统 ===")
    # 接收用户输入并做类型转换
    name = input("请输入您的姓名：")
    age = int(input("请输入您的年龄："))
    height = float(input("请输入您的身高（米）："))
    is_graduate = input("您是否已经毕业？（是/否）：") == "是"

    # 格式化输出信息卡片
    print("\n--- 个人信息卡片 ---")
    print(f"姓 名：{name}")
    print(f"年 龄：{age}岁")
    print(f"身 高：{height}m")
    print(f"状态：{'已毕业' if is_graduate else '在读'}")
    print("-------------------")


if __name__ == '__main__':
    user_info_collect()
