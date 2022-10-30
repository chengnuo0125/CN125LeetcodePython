"""给你一个字符串 jewels代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。
stones中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
字母区分大小写，因此 "a" 和 "A" 是不同类型的石头。
"""


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    # sum 可以直接写表达式
    return sum(stones.count(i) for i in jewels)


print(num_jewels_in_stones("aA", "aAAbbbb"))
