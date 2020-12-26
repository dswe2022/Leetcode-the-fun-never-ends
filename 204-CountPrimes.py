# Leetcode 204
# Easy 12/26/20 

# Count the number of prime numbers less than a non-negative number, n.

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:

# Input: n = 0
# Output: 0

# Example 3:

# Input: n = 1
# Output: 0


class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        isPrime[:2] = [False, False]
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i: n: i] = [False] * len(isPrime[i * i: n: i])
        return sum(isPrime)        


# T: O(a)
# S: O(a)