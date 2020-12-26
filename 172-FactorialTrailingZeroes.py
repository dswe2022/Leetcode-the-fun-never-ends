# Leetcode 172. Factorial Trailing Zeroes
# Easy 12/25/20


# Given an integer n, return the number of trailing zeroes in n!.
# Follow up: Could you write a solution that works in logarithmic time complexity?

# Solution using Recursion

class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else n // 5 + self.trailingZeroes(n // 5)

# T: O(a), number of place holders of digit n.
# S: O(1)