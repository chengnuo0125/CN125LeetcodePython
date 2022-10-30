"""切比雪夫距离"""


def minTimeToVisitAllPoints(points) -> int:
    time = 0
    for i in range(len(points) - 1):
        dx = abs(points[i][0] - points[i + 1][0])
        dy = abs(points[i][1] - points[i + 1][1])

        time += max(dx, dy)
    return time
