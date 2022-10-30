"""给你两个字符串：ransomNote 和 magazine ，
判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
"""


def can_construct(ransomNote: str, magazine: str) -> bool:
    for i in set(ransomNote):
        if magazine.count(i) < ransomNote.count(i):
            return False
    return True


print(can_construct(ransomNote="aa", magazine ="ab"))
