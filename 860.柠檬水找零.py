"""
在柠檬水摊上，每一杯柠檬水的售价为5美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回true，否则返回 false。
"""
from typing import List


def lemonade_change(bills: List[int]) -> bool:
    bank = []
    for i in bills:
        
        if i == 5:
            bank.append(5)
        elif i == 10:
            if bank.count(5) == 0:
                return False
            else:
                bank.append(10)
                bank.remove(5)
        elif i == 20:
            if bank.count(10) > 0 and bank.count(5) > 0:
                bank.remove(10)
                bank.remove(5)
                bank.append(20)
            elif bank.count(5) >= 3:
                for n in range(3):
                    bank.remove(5)
                bank.append(20)
            else:
                return False
    return True


print(lemonade_change([5, 5, 10]))
