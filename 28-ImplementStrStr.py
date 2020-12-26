# Leetcode 28 Implement strStr()
# Easy 12/25/20 



# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when 
# needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1 - l2 + 1):
            if haystack[i:i+l2] == needle: return i
        return -1


# T: O(a)
# S: O(1)

