"""
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
输入为三个整数：day、month 和 year，分别表示日、月、年。
您返回的结果必须是这几个值中的一个
{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
"""


def day_of_the_week(day: int, month: int, year: int) -> str:
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if month == 1 or month == 2:
        y = (year - 1) % 100
        m = month + 12
        c = (year - 1) // 100
    else:
        m = month
        y = year % 100
        c = year // 100
    d = day
    return week[(c//4 - 2*c + y + y//4 + (13*(m+1))//5 + d - 1) % 7]





