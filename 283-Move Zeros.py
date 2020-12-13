# Leetcode 283 Move Zeros 
# Easy 12/13/20 

class Solution(object):
    def moveZero(self,nums):
        count = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[count] = nums[i]
                count += 1
        while count < len(nums):
            nums[count] = 0
            count += 1

# Time: O(a)
# Space: O(1)