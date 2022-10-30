"""给定两个数组 nums1 和 nums2 ，返回 它们的交集 。
输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
 """


def intersection(nums1: list, nums2: list) -> list:
    return list(set(nums1).intersection(set(nums2)))


print(intersection([1, 2, 2, 1], [2, 2]))
