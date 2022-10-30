"""给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。"""


def is_power_of_4(n) -> bool:
    from math import log
    if n <= 0:
        return False
    elif log(n, 4) == int(log(n, 4)):
        return True
    return False


print(is_power_of_4(0))
