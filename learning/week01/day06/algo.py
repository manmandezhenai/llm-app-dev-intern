"""
题目名称：实现 strStr()
题目描述：给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回 -1。
当 needle 是空字符串时，我们应当返回 0。

解题思路：
采用暴力匹配法，逐个检查原串中所有可能的起始位置：
1. 先处理边界情况：模式串为空返回0，模式串比原串长返回-1
2. 遍历原串所有可能的起始下标i，范围为0到原串长度减模式串长度
3. 对于每个i，截取原串中从i开始、长度等于模式串的子串，与模式串比较
4. 如果相等则直接返回当前下标i，遍历结束未找到则返回-1
该方法逻辑简单直观，适合入门理解字符串匹配基础逻辑

时空复杂度：
- 时间复杂度：O(n*m)，n为原串长度，m为模式串长度，最坏情况每个位置都比较m个字符
- 空间复杂度：O(1)，只使用常数级别的额外变量
"""


def str_str(haystack, needle):
    """
    在haystack中查找needle第一次出现的下标
    :param haystack: 原字符串
    :param needle: 要查找的模式字符串
    :return: 第一个匹配的下标，未找到返回-1
    """
    n = len(haystack)
    m = len(needle)

    # 边界处理
    if m == 0:
        return 0
    if m > n:
        return -1

    # 遍历所有可能的起始位置
    for i in range(n - m + 1):
        # 截取子串比较
        if haystack[i: i + m] == needle:
            return i

    return -1


if __name__ == '__main__':
    # 测试用例1：开头匹配
    print(f"测试用例1：{str_str('sadbutsad', 'sad')}")

    # 测试用例2：中间匹配
    print(f"测试用例2：{str_str('hello', 'll')}")

    # 测试用例3：不匹配
    print(f"测试用例3：{str_str('leetcode', 'leeto')}")

    # 测试用例4：空模式串
    print(f"测试用例4：{str_str('abc', '')}")
