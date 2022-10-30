"""
给定一个字符串 s
你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""


def reverse_words(s: str) -> str:
    return " ".join([i[::-1] for i in s.split()])


print(reverse_words("Let's take LeetCode contest"))
