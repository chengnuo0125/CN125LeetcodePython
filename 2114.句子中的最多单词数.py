"""
一个 句子由一些 单词以及它们之间的单个空格组成，句子的开头和结尾不会有多余空格。
给你一个字符串数组 sentences，其中 sentences[i] 表示单个 句子。
请你返回单个句子里 单词的最多数目。
"""
from typing import List


def most_words_found(sentences: List[str]) -> int:
    return max(i.count(" ")+1 for i in sentences)



