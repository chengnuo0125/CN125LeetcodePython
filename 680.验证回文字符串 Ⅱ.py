"""给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。"""

"""
两个指针i、j，i从左向右， j从右向左
判断指针所指字母是否相等
如果全部相等，说明是回文字符串
如果不相等，即s[i] != s[j]
那应该删除其中一个
分别把两种删除后的字符串写下来
看看两者是否有一者是回文字符串"""


def valid_palindrome(s: str) -> bool:
    for i in range(l := len(s)):
        if s[i] != s[j := l - i - 1]:
            a = s[:i] + s[i + 1:]
            b = s[:j] + s[j + 1:]
            return a[::-1] == a or b[::-1] == b
    return True


print(valid_palindrome("eccer"))
