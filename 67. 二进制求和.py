"""给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。
"""


def addition(a, b):
    s = bin(int(a, 2) + int(b, 2))
    return s[2:]


print(addition("10", "1"))
