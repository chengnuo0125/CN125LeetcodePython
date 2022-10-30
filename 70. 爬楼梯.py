"""假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

import math


# 1阶 ： 1种
# 2阶 ： 2种
# 3阶 ： 3种
# 4阶 ： 5种
# 直接用斐波那契数列的通项公式
def stairs(n):
    return int(1 / math.sqrt(5) * (((1 + math.sqrt(5)) / 2) ** (n + 1) - ((1 - math.sqrt(5)) / 2) ** (n + 1)))


print(stairs(10))
