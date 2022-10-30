"""
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
"""


def transpose(matrix):
    return [list(i) for i in zip(*matrix)]


"""
*matrix, 将 matrix 拆分开来
a = [[1,2],[3,4]]
print(*a)
>>> [1,2] [3,4]

list(zip([1,3],[2,4]))
>>> [(1,2), (3,4)]
zip()将每组中位置相同的元素合并起来
"""

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
