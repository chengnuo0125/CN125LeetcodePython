"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。
如果是，返回 true ；否则，返回 false 。
整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
"""


def is_power_of_three(n: int) -> bool:
    if n <= 0: return False
    from math import log
    result = int(log(n, 3))
    if pow(3, result) == n or pow(3, result+1) == n:
        return True
    return False


print(is_power_of_three(243))
