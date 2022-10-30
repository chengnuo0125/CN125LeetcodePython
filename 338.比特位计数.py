"""给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数
返回一个长度为 n + 1 的数组 ans 作为答案
"""


def count_bits(n: int) -> list:
    s = [bin(i).count("1") for i in range(n+1)]
    return s


print(count_bits(5))
