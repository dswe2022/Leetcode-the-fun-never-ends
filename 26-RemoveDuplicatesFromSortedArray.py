# Leetcode 26 Remove Duplicates from sorted Array
# Easy 12/18/20

# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.


# Solution 1

# Solution 1: Two-pointer
# The idea for such problem is that we will set two pointer,
# the faster one will go through the elements in list. The slower one
# only move when meeting the unique number.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        j=1 #slow pointer
        for i in range(1,len(nums)):
            if nums[i] != nums[[]]:
                nums[j] = nums[i]
                j +=1
        
        return j


# Time: O(a)
# Space: O(a)




# Solution 2
# Delete the duplicates in memory
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1
        
        for delete_index in range(i, j-1,-1):
            del nums[delete_index]
        
        return j
        
# Time: O(a)
# Time: O(a)

    
        
