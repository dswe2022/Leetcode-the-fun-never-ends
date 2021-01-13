# Leetcode 1.) Two Sum
# Easy 12/18/20

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for a,num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target-num],i]
                break
            hash_table[num] = i

        return []

    
# Time: O(a)
# Space: O(a)