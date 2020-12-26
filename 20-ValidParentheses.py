# Leetcode 20 Valid Parentheses
# Easy 12/25/20


# Given a singly linked list, determine if it is a palindrome.
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Solution 1
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []	
        hash = {}
        hash["}"] = "{"
        hash["]"] = "["
        hash[")"] = "("
        if len(s) %2 != 0:
            return False
        #iterate through the string: s
        for idx in range(len(s)):
          if s[idx] not in hash.keys():
            stack.append(s[idx])
          else:
            #closing paren,bracket,curly braces.
            #pop the stack and check using hash
            if len(stack) != 0:
                inspectedEle = stack.pop()
                if inspectedEle != hash[s[idx]]:
                    return False
            else:
                return False
        return len(stack) == 0 

# Time: O(a)
# Space: O(a)



# Solution 2
# Similar to solution 1 except it is cleaner.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:stack.append(char)
        return not stack

# T: O(a)
# S: O(a)