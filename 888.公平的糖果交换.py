"""
爱丽丝和鲍勃拥有不同总数量的糖果
给你两个数组 aliceSizes 和 bobSizes
aliceSizes[i] 是爱丽丝拥有的第 i 盒糖果中的糖果数量
bobSizes[j] 是鲍勃拥有的第 j 盒糖果中的糖果数量
两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果
一个人拥有的糖果总数量是他们每盒糖果数量的总和
返回一个整数数组 answer
其中 answer[0] 是爱丽丝必须交换的糖果盒中的糖果的数目，answer[1] 是鲍勃必须交换的糖果盒中的糖果的数目。
如果存在多个答案，你可以返回其中 任何一个 。
题目测试用例保证存在与输入对应的答案。
"""
from typing import List


def fair_candy_swap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    alice_sum, bob_sum = sum(aliceSizes), sum(bobSizes)
    for i in bobSizes:
        if (m := (alice_sum - bob_sum) // 2 + i) in aliceSizes:
            return [m, i]


print(fair_candy_swap([1, 1], [2, 2]))
