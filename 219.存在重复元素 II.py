"""
给你一个整数数组nums 和一个整数k ，
判断数组中是否存在两个 不同的索引i和j ，
满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
如果存在，返回 true ；否则，返回 false 。
"""


def contains_nearby_duplicate(nums:list, k:int) -> bool:
    box = []
    for i in nums:
        box.append(i)
        if len(box) == k+2:
            box = box[1:].copy()
        if box.count(i) != 1:
            return True
    return False


print(contains_nearby_duplicate([1, 0, 1, 1], 1))
