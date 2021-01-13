# Leetcode 322 CoinChange 
# Easy 12/14/20 

class Solution(object):
    def coinChange(self, coins, amount):
        rs = [amount + 1] * (amount + 1)
        rs[0] = 0
        for i in xrange(1, amount + 1):
            for x in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)
        
        if rs[amount] == amount + 1:
            return -1
        return rs[amount]


    

# Time: O(a*b), a is number of elements -1 and b is number of elements in coins.
# Space: O(k), k is number of elements in coin.
