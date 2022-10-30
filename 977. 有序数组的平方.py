"""给你一个按非递减顺序排序的整数数组nums
返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])


s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))



