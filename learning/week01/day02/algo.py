"""
题目名称：反转字符串
题目描述：给定一个字符串 s ，返回该字符串反转后的结果。

解题思路：
采用双指针对撞法实现字符串反转：
1. 由于Python字符串不可变，先将字符串转换为列表，支持字符交换
2. 初始化左指针left=0指向字符串头部，右指针right=len(s)-1指向尾部
3. 当left < right时，交换两个指针对应位置的字符
4. 左指针右移一位，右指针左移一位，循环直到指针相遇
5. 最后将列表转换回字符串返回
该方法逻辑清晰，是字符串反转的经典实现方式

时空复杂度：
- 时间复杂度：O(n)，n为字符串长度，最多遍历n/2次字符交换
- 空间复杂度：O(n)，需要额外列表存储字符，Python字符串不可变无法原地修改
"""


def reverse_string(s):
    """
    反转输入的字符串并返回结果
    :param s: 输入的原始字符串
    :return: 反转后的字符串
    """
    char_list = list(s)
    left = 0
    right = len(char_list) - 1

    while left < right:
        # 交换左右指针对应字符
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    return ''.join(char_list)


if __name__ == '__main__':
    # 测试用例1：常规多字符场景
    print(f"测试用例1：{reverse_string('hello')}")

    # 测试用例2：单个字符场景
    print(f"测试用例2：{reverse_string('a')}")

    # 测试用例3：包含大小写与特殊字符
    print(f"测试用例3：{reverse_string('AI-Engineer!')}")

    # 测试用例4：空字符串场景
    print(f"测试用例4：{reverse_string(repr(''))}")
