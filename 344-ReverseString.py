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

# In-place memory means transforming input in the case the string without using any auxiliary data structure.
# The classical way to solve this in-place memory in using recursion or calling a recursive function without any 
# auxiliary data structure.

# The recursion stack doesn't make it constant space.

# Algorithm:
# a.) Implement a helper function
#     which gets two arrows left and right as arguments
# b.) Base case if left >= right , do nothing
# c.) Otherwise, swap s[left] and s[right] and call helper(left + 1, right - 1)