# Leetcode 322 CoinChange 
# Medium 12/14/20, 1/14/21

# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:

# Input: coins = [2], amount = 3
# Output: -1

# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

# Example 4:

# Input: coins = [1], amount = 1
# Output: 1

# Example 5:

# Input: coins = [1], amount = 2
# Output: 2

 

# Constraints:

#     1 <= coins.length <= 12
#     1 <= coins[i] <= 231 - 1
#     0 <= amount <= 104

# Solution 1 Bottom-up Dyanamic Programming approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        rs = [amount + 1] * (amount + 1)
        rs[0] = 0
        for i in range(1, amount + 1):
            for x in coins:
                if i >= x:
                    rs[i] = min(rs[i], rs[i-x] + 1)
        
        if rs[amount] == amount +1:
            return -1
        return rs[amount]
    

# Time: O(a*b), a is number of elements -1 and b is number of elements in coins.
# Space: O(k), k is number of elements in coin.




# Solution 2
# Top-Down recursive with cacheing
# Time limit exceeded.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount +1)
        dp[0] = 0
        def dfs(a):
            if a < 0:
                return a
            for c in coins:
                res = dfs(a - c)
                if res >= 0:
                    dp[a] = min(dp[a],  1 + res)
            return dp[a] if dp[a] < amount + 1 else -1
        return dfs(amount)







# Solution 3 2-D state transition equation:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        "Method 0, self done, 0-1 knapsack"
        comp = lambda x, y: y if x == 0 else min(x, y)
        coins.sort(reverse=True)
        limit = amount + 1
        dp = [0 for _ in range(limit)]
        dp[0] = 1
        for coin in coins:
            for col in range(coin, limit):
                if dp[col - coin] > 0:
                    dp[col] = comp(dp[col], 1 + dp[col - coin])
        return dp[-1] - 1

# If we ignore the zeros in dp array, 2-D state transition equation (row = coin):
# dp[row][col] = min(dp[row][col], dp[row][col - coin] + 1

# Then I truncated the 2-D equation to 1-D because the calculation is done row by row, col by col.
# So the 1-D state transition equation:
# dp[col] = min(dp[col], dp[col - coin] + 1)

# Now that the num in dp array means the amount of objects that is already in the knapsack. Intuitively, it should starts from zero and it adds up later. However, in that way, min(0, anything) = 0. So I generated the comp function to solve this problem.

# In the beginning, when we have 0 items in the knapsack, we have 0 weight. To distinguish from all other states, I set the start state (0 item, 0 weight) to have 1 item with 0 weight. In this case, all over the calculation, the valid dp state would always have item number bigger than 0. Remember to remove this virtual item from the knapsack in the end.

# Also, didn't think it through why sorting the coins would make code faster.
