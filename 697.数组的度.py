"""
给定一个非空且只包含非负数的整数数组nums，数组的 度 的定义是指数组里任一元素出现频数的最大值。
你的任务是在 nums 中找到与nums拥有相同大小的度的最短连续子数组，返回其长度。
"""
from typing import List


def find_shortest_sub_array(nums: List[int]) -> int:
    from collections import Counter

    left, right, counts = {}, {}, Counter(nums)
    degree = max(counts.values())
    for l in set(nums):
        left.setdefault(l, nums.index(l))
        right.setdefault(l, len(nums) + nums[::-1].index(l) * (-1) - 1)

    return min([right[i] - left[i] + 1 for i, j in counts.items() if j == degree])


print(find_shortest_sub_array([1, 2, 2, 3, 1]))
