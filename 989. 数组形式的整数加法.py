"""
整数的数组形式 num 是按照从左到右的顺序表示其数字的数组。
例如，对于 num = 1321 ，数组形式是 [1,3,2,1] 。
给定 num ，整数的 数组形式 ，和整数 k ，返回 整数 num + k 的 数组形式 。
"""
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_int = ""
        for i in num:
            num_int += str(i)
        num_int = int(num_int)

        total = str(num_int + k)

        return [int(j) for j in total]


s = Solution()
print(s.addToArrayForm(num = [1,2,0,0], k = 34))







