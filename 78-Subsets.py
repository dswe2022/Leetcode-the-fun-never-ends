# Leetcode 78 Subsets 
# Medium 12/26/20


# Given an integer array nums, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets.



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res


# T: O(a)
# S: O(a)
