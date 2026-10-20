"""
Week01-Day04 Python函数基础示例代码
包含：函数定义、参数类型、返回值、作用域、lambda标准化示例 + 成绩计算工具包综合练习
"""

# ---------------------- 第一部分：知识点标准化示例 ----------------------
# 1. 基础函数与返回值
print("=== 1. 基础函数与返回值演示 ===")


def add(a, b):
    """两个数相加，返回和"""
    return a + b


result = add(3, 5)
print(f"add(3, 5) = {result}")


# 无return默认返回None
def print_hello():
    print("Hello World！")


res = print_hello()
print(f"无return函数返回值：{res}")

# 2. 参数类型演示
print("\n=== 2. 函数参数类型演示 ===")


# 默认参数
def greet(name, msg="你好"):
    return f"{msg}，{name}！"


print(greet("张三"))
print(greet("李四", "早上好"))


# 可变关键字参数
def calc_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


print(f"calc_sum(1, 2, 3, 4) = {calc_sum(1, 2, 3, 4)}")


# 可变关键字参数
def print_user(**kwargs):
    for k, v in kwargs.items():
        print(f"    {k}：{v}")


print("用户信息：")
print_user(name="王五", age=22, major="计算机")

# 3. 多返回值
print("\n=== 3. 多返回值演示 ===")


def calc_stat(num_list):
    """计算数值列表的总和、平均值、最大值"""
    total = sum(num_list)
    avg = total / len(num_list)
    max_val = max(num_list)
    return total, avg, max_val


nums = [10, 20, 30, 40]
total, avg, max_val = calc_stat(nums)
print(f"总和：{total}，平均值：{avg}，最大值：{max_val}")

# 4. 变量作用域
print("\n=== 4. 变量作用域演示 ===")
global_var = "全局变量"


def test_scope():
    local_var = "局部变量"
    print(f"函数内访问：{local_var}")
    print(f"函数内访问：{global_var}")


test_scope()
print(f"函数外访问：{global_var}")
# print(local_var)  # 局部变量外部不可访问（会报错）

# 5. lambda匿名函数
print("\n=== 5. lambda匿名函数演示 ===")
square = lambda x: x ** 2
print(f"lambda平方计算：{square(5)}")

# 配合sorted使用
students = [("张三", 90), ("李四", 85), ("王五", 95)]
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
print(f"按分数降序排序：{sorted_students}")


# ---------------------- 第二部分：综合实操小练习 ----------------------
def score_calculator_tool():
    """
    综合练习：成绩计算工具包
    功能：封装多个成绩处理函数，实现成绩统计、等级判定、筛选等功能
    技术点：函数封装、多参数、多返回值、lambda、列表推导式
    """
    print("\n=== 综合小练习：成绩计算工具包 ===")
    score_list = [78, 92, 85, 66, 59, 90, 88, 75, 81, 94]

    def get_statistic(scors):
        """计算成绩统计数据：总分、平均分、最高分、最低分"""
        total = sum(scors)
        avg = total / len(scors)
        return total, avg, max(scors), min(scors)

    def get_grade(score):
        """根据分数返回等级"""
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"

    def filter_scores(scores, condition):
        """根据条件筛选成绩"""
        return [s for s in scores if condition(s)]

    # 调用工具函数
    total, avg, max_val, min_val = get_statistic(score_list)
    print(f"总分：{total}")
    print(f"平均分：{avg:.1f}")
    print(f"最高分：{max_val}")
    print(f"最低分：{min_val}")

    print("\n各成绩等级：")
    for score in score_list:
        print(f" {score}分 → {get_grade(score)}")

    # 用lambda作为筛选条件
    excellent = filter_scores(score_list, lambda score: score >= 90)
    print(f"\n优秀分数列表：{excellent}")
    pass_list = filter_scores(score_list, lambda score: score >= 60)
    print(f"及格率：{len(pass_list) / len(score_list):.1%}")


if __name__ == "__main__":
    score_calculator_tool()
