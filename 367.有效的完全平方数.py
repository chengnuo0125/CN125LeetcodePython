"""给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如sqrt 。
"""


def is_perfect_square(num: int) -> bool:
    if num ** 0.5 == int(num ** 0.5):
        return True
    return False


print(is_perfect_square(76))
