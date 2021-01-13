# Leetcode 279. Perfect Squares
# Medium 12/29/20 

# Given a positive integer n, find the least number of perfect 
# square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.

# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


# Solution 1
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]

# T: O(a*a)
# S: O(a)


# Solution 2
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        level = 0
        queue = {n}
        while queue:
            level += 1
            tmp = set()
            for num in queue:
                for sq in square_nums:    
                    if num == sq:
                        return level
                    elif num < sq:
                        break
                    else:
                        tmp.add(num - sq)
            queue = tmp
# T: O(a*a)
# S: O(a)



# Solution 3
class Solution:
    def numSquares(self, n: int) -> int:
        def check(n):
            return (math.sqrt(n) - int(math.sqrt(n)) < 0.00000001)
            
        if check(n):
            return 1
        while n % 4 == 0:
            n /= 4
        if (n - 7) % 8 == 0:
            return 4
        for i in range(int(math.sqrt(n))):
            if check(n-(i+1)*(i+1)):
                return 2
        return 3

# T: O(a)
# S: O(1)