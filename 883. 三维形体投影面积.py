"""
在 n*n 的网格 grid 中，我们放置了一些与 x,y,z 三轴对齐的 1*1*1 立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i,j) 上。
现在，我们查看这些立方体在 x-y、y-z 和 z-x 平面上的投影。
投影就像影子，将三维形体映射到一个 二维 平面上。
从顶部、前面和侧面看立方体时，我们会看到“影子”。
返回 所有三个投影的总面积 。
"""


def projectionArea(grid) -> int:
    top, front, left = 0, 0, 0
    length = len(grid)

    for i in range(length):

        left += max(grid[i])
        top += (len(grid[i]) - grid[i].count(0))
        front += max(list(zip(*grid))[i])

    return front + left + top


print(projectionArea([[2]]))
