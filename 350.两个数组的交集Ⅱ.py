"""
给你两个整数数组nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致
如果出现次数不一致，则考虑取较小。
可以不考虑输出结果的顺序。
"""


def intersect(nums1: list, nums2: list) -> list:
    s = []
    for i in set(nums1):
        s.extend([i]*min(nums1.count(i), nums2.count(i)))
    return s






print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

