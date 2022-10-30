"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。
返回字符串中最后一个单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
"""


def last_word_length(s):
    s = s[::-1]
    s = s.lstrip()
    s = s.ljust(len(s) + 1, " ")
    return len(s[:s.index(" ")])


print(last_word_length("Hello World"))
print(last_word_length("luffy is still joyboy"))
print(last_word_length("   fly me   to   the moon  "))
print(last_word_length("a "))
