"""给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。
设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""


def maxProfit(prices: list) -> int:
    if not prices: return 0
    mim_prices = max(prices)
    max_profit = 0
    for i in prices:
        if i < mim_prices:
            mim_prices = i
        elif i - mim_prices > max_profit:
            max_profit = i - mim_prices
    return max_profit


print(maxProfit([2, 4, 1]))
