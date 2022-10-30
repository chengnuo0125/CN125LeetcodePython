roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def r2n(x):
    nums_list = [roman[i] for i in x]
    for i in range(len(nums_list) - 1):
        if nums_list[i] < nums_list[i + 1]:
            nums_list[i] *= -1
    return sum(nums_list)


r_nums = input("请输入罗马数字：")
print(r2n(r_nums))
