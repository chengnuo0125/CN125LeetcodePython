"""定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。"""


def lost(nums):
    n = len(nums)
    all_nums = list(range(n + 1))
    for i in all_nums:
        if i not in nums:
            return i


print(lost([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(lost([0]))
print(lost([0, 1]))
print(lost([3, 0, 1]))
