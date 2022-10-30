"""给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""


def generate(rowIndex):
    out = []
    for i in range(rowIndex+1):
        inside = []
        for n in range(i + 1):
            if n == 0 or n == i:
                inside.append(1)
            else:
                inside.append(out[i-1][n] + out[i-1][n-1])
        out.append(inside)
    return out[rowIndex]


print(generate(3))
