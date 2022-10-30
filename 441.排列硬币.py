"""你总共有n枚硬币，并计划将它们按阶梯状排列。
对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。
阶梯的最后一行 可能 是不完整的。
给你一个数字n ，计算并返回可形成 完整阶梯行 的总行数。
"""


def arrange_coins(n: int) -> int:
    length = 0
    for i in range(1, n+1):
        if n > i:
            n -= i
            length += 1
        elif n < i:
            return length
        elif n == i:
            return length + 1


print(arrange_coins(1))