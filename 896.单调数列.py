"""
如果数组是单调递增或单调递减的，那么它是单调 的。
如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。
如果对于所有 i <= j，nums[i]> = nums[j]，那么数组 nums是单调递减的。
当给定的数组 nums是单调数组时返回 true，否则返回 false。
"""
from typing import List


def is_monotonic(nums: List[int]) -> bool:
    return sorted(nums) == nums or sorted(nums, reverse=True) == nums


print(is_monotonic([1,2,2,3]))


