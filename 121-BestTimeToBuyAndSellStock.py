# Leetcode 121. Best Time to Buy and Sell Stock
# Medium 1/14/21


# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

 

# Constraints:

#     1 <= prices.length <= 105
#     0 <= prices[i] <= 104

# Solution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        high=prices[0]
        low=prices[0]
        best=[]
        for i in range(len(prices)):
            if prices[i]>high:
                high=prices[i]
                best.append(high-low)
            if prices[i]<low:
                low=prices[i]
                high=low

        if len(best)>0:
            return max(best)
        return 0

# T: O(a)
# S: O(a)



# Solution 2 Faster

class Solution:
    def maxProfit(self, prices: List[int])-> int:
        # It is impossible to have stock to sell on first day, so -infinity is set as initial value
        init_hold = -float('inf')
        init_not_hold = 0

        prev_hold = init_hold
        prev_not_hold = init_not_hold

        for stock_price in prices:
            # either keep in hold, or just buy today with stock price
            cur_hold = max(prev_hold, -stock_price)

            # either keep in not holding, or just sell today with stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)

            prev_hold = cur_hold
            prev_not_hold = cur_not_hold

            # maximum profit must be in not-state
        
        return cur_not_hold if prices else 0

        