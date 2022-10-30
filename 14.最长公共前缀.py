def longest_common_prefix(strs):
    if len(strs) == 0:
        return '""'

    length, counts = len(strs[0]), len(strs)
    for i in range(length):
        for j in range(1, counts):
            if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]


words = eval(input("请输入一个英文字符串列表："))
print("最长公共前缀是", end=' ')
print(longest_common_prefix(words))
