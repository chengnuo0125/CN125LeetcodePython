"""
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
"""


def reverse_vowels(s: str) -> str:
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    s1 = list(s)
    a = [i for i in s1 if i in vowels]
    for i in range(len(s1)):
        if s1[i] in vowels:
            s1[i] = a[-1]
            a.pop()
    return "".join(s1)


print(reverse_vowels(s="e"))
