# Leetcode 69 Sqrt(x)
# Easy 12/25/20 

# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, 
# and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1 #[left, right)
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif (mid - 1) ** 2 < x and mid ** 2 >= x:
                return mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left    

# T: O(a)
# S: O(1)