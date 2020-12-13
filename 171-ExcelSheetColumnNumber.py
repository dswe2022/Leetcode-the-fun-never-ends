# Leetcode 171 Excel sheet column Number
# Easy 12/13/20 

class Solution(object):
    def titleToNumber(self,s):
        total = 0
        count = 0
        for i in s[::-1]:
            total+= (ord(i) - 64)*(26 **count)
            count += 1
        return total


# Time: O(a)
# Space: O(1)