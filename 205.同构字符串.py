"""
给定两个字符串s和t，判断它们是否是同构的。
如果s中的字符可以按某种映射关系替换得到t，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
"""


def is_isomorphic(s: str, t: str) -> bool:
    d = {s[i]: t[i] for i in range(len(s))}
    same = []
    for i in d:
        if d[i] in same:
            return False
        same.append(d[i])
    string = ""
    for i in s:
        string += d[i]
    return string == t


print(is_isomorphic(s="egg", t="add"))
print(is_isomorphic(s="foo", t="bar"))
print(is_isomorphic(s="badc", t="baba"))
