"""给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
"""


def my_sqrt(x: int) -> int:
    if x:
        b = x
        for i in range(50):
            b = 0.5 * (b + x / b)
        return int(b)
    return x


x = 2147395599
print(my_sqrt(x))
print(pow(x, 0.5))
