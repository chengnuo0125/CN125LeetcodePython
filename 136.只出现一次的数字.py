"""给定一个非空整数数组，除了某个元素只出现一次以外，
其余每个元素均出现两次。
找出那个只出现了一次的元素。
"""


def once(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i


print(once([4,1,2,1,2]))
