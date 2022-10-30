"""给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。"""


def first_uniq_char(s: str) -> int:
    from collections import Counter
    c = Counter(s)
    for i in c:
        if c[i] == 1:
            return s.find(i)
    return -1


print(first_uniq_char(s = "loveleetcode"))
