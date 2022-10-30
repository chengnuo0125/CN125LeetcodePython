"""颠倒给定的 32 位无符号整数的二进制位。"""


def reverse_bit(n):
    return int(f"{n:032b}"[::-1], 2)


print(reverse_bit(10100101000001111010011100000000))
