"""
给你一个数组 candies 和一个整数 extraCandies，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。
对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多的糖果。
注意，允许有多个孩子同时拥有 最多的糖果数目。
"""
from typing import List


def kids_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
    ans = []
    for i in candies:
        if i + extraCandies >= max(candies):
            ans.append(True)
        else:
            ans.append(False)
    return ans


print(kids_with_candies(candies=[2, 3, 5, 1, 3], extraCandies=3))
