from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    for i in nums1:
        n = nums2.index(i)

        for j in nums2[n + 1:]:
            if j > i:
                ans.append(j)
                break
        else:
            ans.append(-1)

    return ans


print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
