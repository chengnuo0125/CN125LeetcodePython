"""
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
"""
from typing import List


def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    row = len(matrix)
    if len(matrix[0]) == 1 and row == 1:
        return True
    for i in range(row - 1):
        if matrix[i][:-1] != matrix[i + 1][1:]:
            return False
    return True


print(is_toeplitz_matrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
