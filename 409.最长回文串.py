"""
给定一个包含大写字母和小写字母的字符串s，返回通过这些字母构造成的 最长的回文串。
在构造过程中，请注意 区分大小写 。比如"Aa"不能当做一个回文字符串。
"""


def longest_palindrome(s: str) -> int:
    from collections import Counter
    length = 0
    for i in Counter(s).values():
        length += i // 2 * 2
        if length % 2 == 0 and i % 2 == 1:
            length += 1
    return length


print(longest_palindrome("a"))
