"""
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
"""
from typing import List


def largest_triangle_area(points: List[List[int]]):
    length = len(points)
    areas = set()
    for i in range(length - 2):

        for j in range(i + 1, length - 1):

            for m in range(j + 1, length):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                x3 = points[m][0]
                y3 = points[m][1]
                areas.add(x1 * y2 - x1 * y3 + x2 * y3 - x2 * y1 + x3 * y1 - x2 * y2)
    return max(areas)


print(largest_triangle_area([[1, 0], [0, 0], [0, 1]]))
