# Leetcode 122 Best TIme to BUy and sell stock II  
# Easy 12/13/20 

class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        for a in range(1, len(prices)):
            if prices[a] > prices[a-1]:
                maxProfit += prices[a] - prices[a-1]

        return maxProfit


# Time: O(a), linear time
# Space: O(1), constant time

