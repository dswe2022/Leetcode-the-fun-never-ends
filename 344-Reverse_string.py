# Leetcode 344 Reverse String - Easy
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space. Do this in - place memory or O(1) extra memory

# Solution 1

class Solution:
        def reverseString(self,str):
            str.reverse()
            # This does work, but uses a library function. 
            # Need to use in-place and two arrow approach.



# Solution 2 

class Solution:
        def reverseString(self, s):
            def helper(left, right):
                if left < right:
                    s[left] = s[right]
                    s[right] = s[left]
                    helper(left+1, right -1)
            helper(0, len(s) - 1)

# Does in place mean constant space complexity?
# Constant space complexity means O(1)
# No, in-place memory can mean O(a) or using more than O(1) memory.

