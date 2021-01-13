# Leetcode 5. Longest Palindromic Substring
# Medium 1/5/21

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Example 3:

# Input: s = "a"
# Output: "a"

# Example 4:

# Input: s = "ac"
# Output: "a"

 

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters (lower-case and/or upper-case),



# Solution 1

class Solution:
    def getLongestPalindrome(self,s,l,r):
        while l>=0 and r< len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        for i in range(len(s)):
            len1 = len(self.getLongestPalindrome(s,i,i))
            if len1 > len(palindrome):
                palindrome = self.getLongestPalindrome(s,i,i)
            len2 = len(self.getLongestPalindrome(s,i,i+1))
            if len2 > len(palindrome):
                palindrome  = self.getLongestPalindrome(s,i,i+1)
        return palindrome

# T: O(ab)
# S: O(1)



# Solution 2


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
             P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
             # Attempt to expand palindrome centered at i
             while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                 P[i] += 1
                # If palindrome centered at i expand past R,
                # adjust center based on expanded palindrome.
             if i + P[i] > R:
                C, R = i, i + P[i]
    
     # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]

# T: O(a^2)
# S: O(a)