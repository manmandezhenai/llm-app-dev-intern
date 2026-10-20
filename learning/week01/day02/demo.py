"""
Week01-Day02 Python核心数据结构示例代码
包含：列表、元组、字典、集合标准化示例 + 学生成绩管理综合练习
"""

# ---------------------- 第一部分：知识点标准化示例 ----------------------
# 1. 列表操作
print("=== 1. 列表操作演示 ===")
num_list = [10, 20, 30, 20]
print(f"原始列表：{num_list}")

# 增加元素
num_list.append(40)
print(f"append尾部追加：{num_list}")
num_list.insert(1, 15)
print(f"insert指定位置插入：{num_list}")

# 删除元素
pop_value = num_list.pop(0)
print(f"pop删除下标0元素：{num_list}，删除的值：{pop_value}")
num_list.remove(20)
print(f"remove删除第一个20：{num_list}")

# 切片与反转
print(f"切片[1:3]：{num_list[1:3]}")
num_list.reverse()
print(f"reverse原地反转：{num_list}")

# 2. 元组操作
print("\n=== 2. 元组操作演示 ===")
user_info = ("张三", 22, "计算机专业")
print(f"完整元组：{user_info}")
print(f"索引取值：{user_info[0]}")
print(f"切片[1:]：{user_info[1:]}")
print(f"元素计数：22出现次数 = {user_info.count(22)}")

# 元组不可修改
# user_info[0] = "李四"   # TypeError: 'tuple' object does not support item assignment

# 3. 字典操作
print("\n=== 3.字典操作演示 ===")
student = {"name": "李四", "age": 21, "score": 90}
print(f"原始字典：{student}")

# 增改操作
student["gender"] = "男"
student["score"] = 95
print(f"新增 + 修改后：{student}")

# 取值操作
print(f"get取值name：{student.get('name')}")
print(f"get取不存在的键：{student.get('grade', '未知')}")

# 遍历键值对
print("\n遍历键值对：")
for key, value in student.items():
    print(f"    {key}：{value}")

# 4. 集合操作
print("\n=== 4. 集合操作演示 ===")
list_a = [1, 2, 2, 3, 4]
set_a = set(list_a)
print(f"列表转集合自动去重：{set_a}")

set_b = {3, 4, 5, 6}
print(f"集合A：{set_a}，集合B：{set_b}")
print(f"交集：{set_a & set_b}")
print(f"并集：{set_a | set_b}")
print(f"差集（A-B）：{set_a - set_b}")


# ---------------------- 第二部分：综合实操小练习 ----------------------
def score_manage_system():
    """
    综合练习：学生成绩管理小程序
    功能：添加学生、查询成绩、统计平均分、查看所有学生
    技术点：列表嵌套字典、循环、条件判断、字典操作
    """
    print("\n=== 综合小练习：学生成绩管理系统 ===")
    student_list = []

    while True:
        print("\n功能菜单：")
        print("1. 添加学生")
        print("2. 查询学生成绩")
        print("3. 统计班级平均分")
        print("4. 查看所有学生")
        print("0. 退出系统")
        choice = input("请输入功能编号：")

        if choice == "1":
            name = input("请输入学生姓名：")
            score = int(input("请输入学生成绩："))
            student = {"name": name, "score": score}
            student_list.append(student)
            print(f"学生【{name}】添加成功！")

        elif choice == "2":
            name = input("请输入要查询的学生姓名：")
            for stu in student_list:
                if stu["name"] == name:
                    print(f"姓名：{stu['name']}，成绩：{stu['score']}")
                    break
            else:
                print("未找到该学生！")

        elif choice == "3":
            if len(student_list) == 0:
                print("暂无学生数据！")
                continue
            total = sum(stu["score"] for stu in student_list)
            avg = total / len(student_list)
            print(f"班级总人数：{len(student_list)}，平均分：{avg:.1f}")

        elif choice == "4":
            if not student_list:
                print("暂无学生数据！")
                continue

            print("所有学生列表：")
            for index, stu in enumerate(student_list, 1):
                print(f"    {index}. {stu['name']} - {stu['score']}分")

        elif choice == "0":
            print("退出系统！")
            break

        else:
            print("输入无效，请重新选择！")


if __name__ == '__main__':
    score_manage_system()
