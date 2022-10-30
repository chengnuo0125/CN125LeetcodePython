"""给定一种规律 pattern和一个字符串s，判断 s 是否遵循相同的规律。
这里的遵循指完全匹配，例如，pattern里的每个字母和字符串str中的每个非空单词之间存在着双向连接的对应规律。
"""


def word_pattern(pattern: str, s: str) -> bool:
    return len(pattern) == len(s1 := s.split(" ")) and len(set(zip(list(pattern), s1))) == len(set(pattern)) == len(
        set(s1))


print(word_pattern(pattern="abba", s="dog cat cat dog"))
