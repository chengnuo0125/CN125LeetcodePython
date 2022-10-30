"""给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


def and_one(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            for j in range(i+1, n):
                digits[j] = 0
            return digits
    return [1] + [0] * n


print(and_one([9]))
print(and_one([1, 2, 3]))
print(and_one([4, 3, 1, 2]))
