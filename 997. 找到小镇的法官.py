"""
小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。
如果小镇法官真的存在，那么：
    1.小镇法官不会信任任何人。
    2.每个人（除了小镇法官）都信任这位小镇法官。
    3.只有一个人同时满足属性 1 和属性 2 。

给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
"""
from typing import List

"""
想象一张网格图，每个人是图上的一个节点，从一个节点 a 指向另一个节点 b 的箭头表示 a 信任 b，也就是输入中的 [a, b]
指向一个节点的箭头数量表示这个人被多少人信任，记作这个节点的 入度
从一个节点出发指向其他节点的箭头数量表示这个人信任多少人，记作这个节点的 出度
法官不信任任何人，那么他的出度为 0
每个人（除了小镇法官）都信任这位小镇法官， 那么法官的入度为 n-1
"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = {}.fromkeys([i for i in range(1, n + 1)], 0)
        out_degree = {}.fromkeys([i for i in range(1, n + 1)], 0)

        for i in trust:
            out_degree[i[0]] += 1
            in_degree[i[1]] += 1

        for i in range(1, n + 1):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i
        return -1


s = Solution()
print(s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))

