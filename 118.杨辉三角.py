"""给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""


def generate(num_rows):
    outside = []
    for i in range(num_rows):
        inside = []
        for n in range(i+1):
            if n == 0 or n == i:
                inside.append(1)
            else:
                inside.append(outside[i-1][n] + outside[i-1][n-1])
        outside.append(inside)
    return outside


print(generate(3))