"""
给你一个整数数组 nums ，
请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组:数组中的一个连续部分。
"""


# todo leetcode 53

# 暴力法
def forcible_max():
    all_sum = [sum(nums[i:n + 1]) for i in range(len(nums)) for n in range(i, len(nums))]
    return max(all_sum)


# 贪心算法
def greedy_max():
    pass


nums = eval(input("Please input a num list:"))
