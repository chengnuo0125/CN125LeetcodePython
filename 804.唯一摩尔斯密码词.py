"""
给你一个字符串数组 words ，每个单词可以写成每个字母对应摩尔斯密码的组合。
例如，"cab" 可以写成 "-.-..--..." ，(即 "-.-." + ".-" + "-..." 字符串的结合)。
我们将这样一个连接过程称作 单词翻译 。
对 words 中所有单词进行单词翻译，返回不同 单词翻译 的数量。
"""
from typing import List


def unique_morse_representations(words: List[str]) -> int:
    translate_table = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                       "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                       "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                       "y": "-.--", "z": "--.."}
    result = set()
    for word in words:
        s = ""
        for letter in word:
            s += translate_table[letter]
        result.add(s)
    return len(result)


print(unique_morse_representations(words = ["a"]))
