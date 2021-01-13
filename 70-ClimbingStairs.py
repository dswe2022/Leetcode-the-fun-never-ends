# Leetcode 70. Climbing Stairs
# Easy 12/18/20

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        # Build the list using []*(integer) notation.
        dp = [0]*(n+1)
        # Fill the first two.
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Time: O(a)
# Space: O(a)


# If we iterate all dp array, it will cost O(a), each value will add up
# last two value as result,
# it will cost (1+2), in total total will be O( n + 2n) and it is O(a).





