# Leetcode 28. Implement strStr()
# Easy 1/22/21

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:

# Input: haystack = "", needle = ""
# Output: 0


class Solution:
    def strStr(self, haystack: str, needle:str)-> int:
        L = len(needle)
        n = len(haystack)

        for start in range(n - L +1):
            if haystack[start: start + L] == needle:
                return start
        return -1


# T: O((N-L)L), where N is a length of haystack and L is a length of
# needle. We compute a substring of length L in a loop, which executed (N-L) times.

# Space complexity: O(1)







