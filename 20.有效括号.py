def valid_parenthesis(s):
    stack = []
    for i in s:
        if i in ["(", "[", "{"]:
            stack.append(i)
        else:
            if stack and stack[-1]+i in ["()", "[]", "{}"]:
                stack.pop()
            else:
                return False
    return not stack



x = input("请输入一个由括号组成的字符串：")
print(valid_parenthesis(x))
