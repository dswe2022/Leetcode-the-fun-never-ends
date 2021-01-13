# Leetcode 7 Reverse Integer
# Easy 12/26/20 


# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# Solution 1
class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31 -1):
            return 0
        if x < (-2**31):
            return 0
        if x >= 0:
            if int(str(x)[::-1]) <= (2**31 - 1):
                return int(str(x)[::-1])
            return 0
        else:
            if -int(str(x)[-1:0:-1]) >= (-2**31):
                return -int(str(x)[-1:0:-1])
            return 0        




# Solution 2
class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31 -1) or x < (-2**31):
            return 0
        if x >= 0:
            a = 0
            while x != 0:
                a = a * 10 + x % 10
                x = x // 10
            if a <= (2**31 - 1):
                return a
            return 0
        else:
            b = 0
            while x != 0:
                b = b * 10 + (x % -10)
                x = -(x // -10)
            if b >= (-2**31):
                return b
            return 0