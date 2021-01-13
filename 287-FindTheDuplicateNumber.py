# Leetcode 287. Find the Duplicate Number
# Medium 12/27/20


# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one duplicate number in nums, return this duplicate number.

# Follow-ups:

#     How can we prove that at least one duplicate number must exist in nums? 
#     Can you solve the problem without modifying the array nums?
#     Can you solve the problem using only constant, O(1) extra space?
#     Can you solve the problem with runtime complexity less than O(n2)?

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:

# Input: nums = [1,1]
# Output: 1

# Example 4:

# Input: nums = [1,1,2]
# Output: 1



# Solution 1

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
          hare = nums[0]
          tortoise = nums[0]
          while True:
             hare = nums[nums[hare]]
             tortoise = nums[tortoise]
             if hare == tortoise:
                break
          ptr = nums[0]
          while ptr!=tortoise:
             ptr = nums[ptr]
             tortoise = nums[tortoise]
          return ptr

# T: O(a)
# S: O(a)

