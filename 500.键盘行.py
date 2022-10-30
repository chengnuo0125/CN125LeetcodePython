"""
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
美式键盘 中：
第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。
"""
from typing import List


# my answer
def find_words(words: List[str]) -> List[str]:
    one, two, three = "qwertyuiop", "asdfghjkl", "zxcvbnm"
    ans = []
    for i in words:
        s, x = set(), set(i.lower())
        for j in x:
            if j in one:
                s.add(1)
            elif j in two:
                s.add(2)
            else:
                s.add(3)
        if len(s) == 1:
            ans.append(i)
    return ans


print(find_words(words=["omk"]))


# another answer
def find_words(words):
    set1 = set('qwertyuiop')
    set2 = set('asdfghjkl')
    set3 = set('zxcvbnm')
    res = []
    for i in words:
        x = i.lower()
        setx = set(x)
        if setx <= set1 or setx <= set2 or setx <= set3:
            res.append(i)

    return res


print(find_words(words=["aaaAa"]))
