"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。
另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
"""
from typing import List


def next_greatest_letter(letters: List[str], target: str) -> str:
    for i in range(len(letters)):
        if letters[i] > target:
            return letters[i]
    for i in range(len(letters)):
        if letters[i] < target:
            return letters[i]







