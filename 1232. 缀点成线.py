"""给定一个数组 coordinates ，其中 coordinates[i] = [x, y]，
[x, y]表示横坐标为 x、纵坐标为 y 的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上。
"""


def checkStraightLine(coordinates) -> bool:
    # 向量平行定理：x1*y2==x2*y1
    # 如果所有点在同一条直线上，那么第一个点到每个点的向量都应共线
    l = [[coordinates[i][0] - coordinates[0][0], coordinates[i][1] - coordinates[0][1]] for i in
         range(1, len(coordinates))]
    for i in l:
        if l[0][0] * i[1] - l[0][1] * i[0] != 0:
            return False
    return True


print(checkStraightLine([[0, 0], [0, 1], [0, -1]]))
