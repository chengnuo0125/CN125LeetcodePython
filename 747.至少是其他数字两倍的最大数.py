"""
给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。
请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。
"""
from typing import List


def dominant_index(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    m = max(nums)
    for i in set(nums):
        if i != m and i * 2 > m:
            return -1
    return nums.index(m)


print(dominant_index(nums=[3, 6, 1, 0]))
