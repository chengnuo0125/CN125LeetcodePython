"""给定一个大小为 n 的数组，找到其中的多数元素。
多数元素是指在数组中出现次数 大于 n/2 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""


def majority_element(nums: list) -> int:
    nums.sort()
    return nums[int(len(nums)/2)]
