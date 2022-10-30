"""给你一个整数 n，请你判断该整数是否是 2 的幂次方。
如果是，返回 true ；否则，返回 false 。
"""


def is_power_of_two(n: int) -> bool:
    from math import log2
    if n > 0:
        return n == 2 ** int(log2(n))
    return False


print(is_power_of_two(4))
