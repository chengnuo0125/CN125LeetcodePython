"""给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。"""


def third_max(nums: list) -> int:
    s_nums = set(nums)
    if len(s_nums) < 3:
        return max(s_nums)
    return list(sorted(s_nums))[-3]


print(third_max([1, 1, 1, 1]))
