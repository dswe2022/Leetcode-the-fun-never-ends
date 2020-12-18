# Leetcode 121. Best Time to Buy and Sell Stock
# Easy 12/18/20

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.


def maxProfit(prices):
    n = len(prices)
    if n<2:
        return 0
    maxprofit = float('-inf')
    minstock = prices[0]
    for p in prices:
        maxprofit = max(maxprofit, p-minstack)
        minstock = min(minstack, p)
    return maxprofit

    

    