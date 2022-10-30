# 判断一个数是否是回文数
def is_palindrome():
    x = input("请输入：")
    if x == x[::-1]:
        return True
    else:
        return False


print(is_palindrome())
