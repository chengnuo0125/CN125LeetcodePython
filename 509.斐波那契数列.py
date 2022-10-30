"""
斐波那契数（通常用F(n) 表示）形成的序列称为 斐波那契数列 。
该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。
给定n ，请计算 F(n) 。
"""

def fib(n:int)->int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


d = {i:fib(i) for i in range(31)}

print(d)
