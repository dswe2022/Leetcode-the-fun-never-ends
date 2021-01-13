# Leetcode 13 Roman to Integer
# Easy 12/13/20 

# Convert Roman letters to integers
# V -> 5
# X -> 10



class Solution(object):
    def romanToInt(self,s):
        if not s:
            return 0
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}            
        n = len(s)
        total = dic[s[n-1]]
        for i in range(n-1, 0,-1):
            current = dic[s[i]]
            prev = dic[s[i-1]]
            total += prev if prev >= current else -prev

        return total



# Time: O(a), a is number of characters in input s.
# Space: O(1), the dictionary is limited to 7 key:value pairs. 