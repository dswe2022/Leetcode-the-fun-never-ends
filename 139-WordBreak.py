# Leetcode 	139
# Medium 1/1/21

# Given a non-empty string s and a dictionary wordDict containing a list 
# of non-empty words, determine if s can be segmented into a space-separated 
# sequence of one or more dictionary words.

# Note:

#     The same word in the dictionary may be reused multiple times in the segmentation.
#     You may assume the dictionary does not contain duplicate words.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false


# Solution 1
# The main idea is to check if s begins with any dict words. If we find one, strip it off of s and make recursive call with that new s. If we end up with the empty string return true.

# This results in 0(2^n) but if we store every substring in a map that maps to True if we've already solved for that substring, it becomes 0(n^2)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self.helper(s, wordDict, memo)
        
    
    def helper(self, s, wordDict, memo):
        # base case: if word is empty its in dict or we've stripped off every word and result is empty
        if len(s) == 0:
            return True
        elif s in memo:
            return memo[s]
        
        for word in wordDict:
            # check if any words in dictionary are in the beginning of s
            prefix = s[0:len(word)]
            
            # if we found a match, recursive call with that part stripped off
            if prefix == word and self.helper(s[len(word):], wordDict, memo):
                memo[prefix] = True
                return True
                
        memo[s] = False
        return False


# T: O(a)
# S: O(a)

