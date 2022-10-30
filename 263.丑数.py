"""
丑数 就是只包含质因数 2、3 和 5 的正整数。
给你一个整数 n ，请你判断 n 是否为 丑数 。
如果是，返回 true ；否则，返回 false 。
"""


def is_ugly(n: int) -> bool:
    if not n: return False
    factors = set()
    while n % 2 == 0:
        n /= 2
        factors.add(2)
    while n % 3 == 0:
        n /= 3
        factors.add(3)
    while n % 5 == 0:
        n /= 5
        factors.add(5)
    factors.add(n)
    return factors.issubset({1, 2, 3, 5})


print(is_ugly(14))
