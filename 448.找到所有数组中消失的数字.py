"""
给你一个含 n 个整数的数组 nums，其中 nums[i] 在区间 [1, n] 内。
请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
"""


def find_disappeared_numbers(nums: list) -> list:
    return list({i for i in range(1, len(nums) + 1)}.difference(nums))


print(find_disappeared_numbers(nums=[1, 1]))
