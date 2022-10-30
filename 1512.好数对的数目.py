"""
给你一个整数数组 nums 。
如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
返回好数对的数目。
"""
from typing import List


def num_identical_pairs(nums: List[int]) -> int:
    ans = 0
    for i in range((length := len(nums)) - 1):
        for m in range(i+1, length):
            if nums[i] == nums[m]:
                ans += 1
    return ans


print(num_identical_pairs([1]))
