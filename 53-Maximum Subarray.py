# Leetcode 53. Maximum Subarray
# Easy 12/18/20 

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        dp.append(nums[0])
        current_largest_sum = dp[0]
        for a in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            if dp[i] > current_largest_sum:
                current_largest_sum = dp[i]

        return current_largest_sum



# Time: O(a)
# Space: O(a)

