"""某种外星语也使用英文小写字母，但可能顺序 order 不同。
字母表的顺序（order）是一些小写字母的排列。
给定一组用外星语书写的单词 words，以及其字母表的顺序 order，
只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        j = len(words)
        d = {}
        n = 0
        for i in order:
            d[i] = n
            n += 1

        for m in range(j-1):
            for i in range(len(words[m])):
                if d[words[m][0]] < d[words[m+1][0]]:
                    break
                if len(words[m]) > len(words[m+1]) and words[m+1] in words[m]:
                    return False
                if d[words[m][i]] > d[words[m+1][i]]:
                    return False
                elif d[words[m][i]] == d[words[m+1][i]]:
                    continue
        return True

a = Solution()
print(a.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))








