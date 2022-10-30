"""
给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，
如果这些点构成一个回旋镖则返回true。
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
"""


def isBoomerang(points) -> bool:
    a, b, c, d, e, f = *points[0], *points[1], *points[2]
    return -b * c + a * d + b * e - d * e - a * f + c * f != 0


print(isBoomerang([[1, 1], [2, 2], [3, 3]]))
