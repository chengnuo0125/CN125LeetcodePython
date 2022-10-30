"""给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，
其中 second 紧随 first 出现，third 紧随 second 出现。
对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。
"""
from typing import List


def find_ocurrences(text: str, first: str, second: str) -> List[str]:
    text = text.split(" ")
    return [text[i + 2] for i in range(len(text) - 2) if text[i] if text[i + 1] == second]


print(find_ocurrences("alice is a good girl she is a good student", first="a", second="good"))
