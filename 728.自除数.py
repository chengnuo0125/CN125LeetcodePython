"""
自除数是指可以被它包含的每一位数整除的数。
例如，128 是一个 自除数 ，因为128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
自除数 不允许包含 0 。
给定两个整数left和right ，返回一个列表，
列表的元素是范围[left, right]内所有的 自除数 。
"""


def self_dividing_numbers(left: int, right: int) -> list[int]:
    ans = []
    for i in range(left, right + 1):
        count = 0
        si = str(i)
        if si.count("0") == 0:
            for j in si:
                if i % int(j) == 0:
                    count += 1
            if count == len(si):
                ans.append(i)
    return ans


print(self_dividing_numbers(left=47, right=85))
