"""
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数，就返回 true ；不是，则返回 false 。
"""


def is_happy(n):
    def square(num):
        total_sum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total_sum += digit ** 2
        return total_sum

    s = set()
    while n not in s and n != 1:
        s.add(n)
        n = square(n)
    if n == 1:
        return True
    return False


print(is_happy(4))
