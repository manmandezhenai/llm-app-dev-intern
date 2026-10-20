"""
Week01-Day03 Python流程控制与推导式示例代码
包含：条件分支、循环语句、循环控制、推导式标准化示例 + 成绩分级统计综合练习
"""

# ---------------------- 第一部分：知识点标准化示例 ----------------------
# 1. 条件分支
print("=== 1. 条件分支演示 ===")
score = 78
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"分数：{score}，等级：{grade}")

# 三元表达式
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"年龄：{age}，状态：{status}")

# 2. for循环
print("\n=== 2. for循环演示 ===")
print("range(5)生成序列：", end="")
for i in range(5):
    print(i, end=" ")
print()

fruits = ["苹果", "香蕉", "橙子"]
print("\nenumerate遍历列表：")
for index, fruit in enumerate(fruits, 1):
    print(f"    第{index}个：{fruit}")

# 3. 循环控制
print("\n=== 3. 循环控制演示 ===")
print("continue跳过偶数：", end="")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

print("break遇到5终止：", end="")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print()

# 4. 推导式
print("\n=== 4. 推导式演示 ===")
# 列表推导式：生成1-10的平方数列表
square_list = [x ** 2 for x in range(1, 11)]
print(f"1-10平方数列表：{square_list}")

# 带条件判断的列表推导式：筛选奇数
odd_list = [x for x in range(1, 11) if x % 2 != 0]
print(f"1-10奇数列表：{odd_list}")

# 字典推导式：字符串长度映射
words = ["Python", "Java", "Go", "JavaScript"]
len_dict = {word: len(word) for word in words}
print(f"字符串长度字典：{len_dict}")


# ---------------------- 第二部分：综合实操小练习 ----------------------
def score_grade_statistics():
    """
    综合练习：成绩分级统计系统
    功能：输入学生成绩列表，统计各等级人数，生成各等级学生名单
    技术点：循环、条件分支、列表推导式、字典操作
    """
    print("\n=== 综合小练习：成绩分级统计系统 ===")
    # 模拟学生成绩数据
    student_scores = [
        {"name": "张三", "score": 95},
        {"name": "李四", "score": 82},
        {"name": "王五", "score": 76},
        {"name": "赵六", "score": 58},
        {"name": "孙七", "score": 88},
        {"name": "周八", "score": 65},
        {"name": "吴九", "score": 91},
        {"name": "郑十", "score": 49}
    ]

    # 初始化各等级名单
    grade_info = {
        "优秀": [],
        "良好": [],
        "及格": [],
        "不及格": []
    }

    # 遍历成绩进行分级
    for student in student_scores:
        score = student["score"]
        name = student["name"]
        if score >= 90:
            grade_info["优秀"].append(name)
        elif score >= 80:
            grade_info["良好"].append(name)
        elif score >= 60:
            grade_info["及格"].append(name)
        else:
            grade_info["不及格"].append(name)

    # 输出统计结果
    print("各等级人数统计：")
    for grade, names in grade_info.items():
        print(f"    {grade}：{len(names)}人，名单：{names}")

    # 用推导式快速筛选及格学生
    pass_names = [stu["name"] for stu in student_scores if stu["score"] >= 60]
    print(f"\n列表推导式筛选及格学生：{pass_names}")

    # 计算平均分
    total_score = sum(student["score"] for student in student_scores)
    avg_score = total_score / len(student_scores)
    print(f"班级平均分：{avg_score:.1f}")


if __name__ == "__main__":
    score_grade_statistics()
