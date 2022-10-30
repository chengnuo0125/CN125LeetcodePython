"""
给定一个非负整数数组 nums，nums 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 nums[i] 为奇数时，i 也是 奇数 ；当 nums[i] 为偶数时， i 也是偶数。
你可以返回 任何满足上述条件的数组作为答案 。
"""
from typing import List


def sort_array_by_parity_2(nums: List[int]) -> List[int]:
    tow, one, ans = [], [], []
    for i in nums:
        if i % 2:
            one.append(i)
        else:
            tow.append(i)
    for i in range(len(nums)):
        if i % 2 == 0:
            ans.append(tow.pop())
        else:
            ans.append(one.pop())
    return ans


print(sort_array_by_parity_2([4, 2, 5, 7]))
