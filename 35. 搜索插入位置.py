"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
"""


def look_for(nums, target):
    seat = nums.count(target)
    if seat == 0:
        nums.append(target)
        nums.sort()
        return nums.index(target)
    else:
        return nums.index(target)


nums = eval(input("Please input a list:"))
target = int(input("Please input a integer:"))

print(look_for(nums, target))
