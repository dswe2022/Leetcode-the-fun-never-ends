# Leetcode 3. Longest Substring Without Repeating Characters

# Medium 1/5/21

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:

# Input: s = ""
# Output: 0

 

# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

# Solution 1
# Simple Python Sliding window technique

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0 or s==None:
            return 0
        if len(s) == 1:
            return 1
  
        set1 = set()
        #Two pointers
        left=0
        right=0
        ans=0
        
        while left < len(s) and right < len(s):
            #try to extend the range [i,j]

            print("right: "+str(right))
            print("left: "+str(left))
            try:
                if s[right] not in set1:
                    set1.add(s[right])
                    right+=1
                    ans = max(ans, right-left)
                else:
                    set1.remove(s[left])
                    left+=1
            except IndexError:
                pass
        return ans

# Two pointer method
# T: O(a)
# S: O(a)



# Solution 2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        right = 0
        left = 0
        ans =0
        while right<len(s) and left<len(s):
            try:
                if s[right] not in set1:
                    set1.add(s[right])
                    right+=1
                    ans = max(ans, right-left)
                
                else:
                    set1.remove(s[left])
                    left+=1
                    
            except IndexError:
                pass
        return ans

# T: O(a)
# S: O(a)