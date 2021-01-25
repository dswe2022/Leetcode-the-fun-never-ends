# Leetcode 238. Product of Array Except Self
# Medium 12/26/20


# Given an array nums of n integers where n > 1,  return an array output 
# such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of 
# the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra 
# space for the purpose of space complexity analysis.)

# This question solved by Dynamic Programming.

# This question is not hard to solve, even brute force will not give you a bad performance, the brute force will cost O(n^2). However, the question ask you to solve it in O(n), that means you can only iterate in linear time. So we choose DP array. There is a better readable solution that I will show you later
# Basic Idea

# The basic idea is really easy understand.

# For each current value except itself can divide into two parts: the previous total product and next total product.

# The basic idea here is previous total product multiple next total product will return the expected value in the current position.

# In classic way, we need to generate two lists, one for previous total product, the other one is for next total product, then we multiple two elements with same index to get the value we wanted.

# Or in this solution, we can generate previous total product as output first, then go through the output again to multiple each next product to save space.

# I would say this is more like a dynamic programming question implicitly.


# Solution 1

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start, end, n = 1, 1, len(nums)
        out = [1]*n 
        for i in range(n):
            out[i] *= start
            start *= nums[i]
            out[~i] *= end
            end *= nums[~i]
        return out

# T: O(a), iterate through dp array.
# S: O(a)


# Solution 2

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L,R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1,length):
            L[i] = nums[i-1]*L[i-1]
        R[length - 1] = 1
        for i in reversed(range(length -1)):
            R[i] = nums[i+1] * R[i+1]
            
            
        for i in range(length):
            answer[i] = L[i] * R[i]
            
        return answer