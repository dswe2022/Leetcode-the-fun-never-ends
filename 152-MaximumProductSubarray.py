# Leetcode 152. Maximum Product Subarray

# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        max_here = min_here = max_so_far = nums[0]
        for i in range(1, len(nums)):
            mx, mn = max_here, min_here
            max_here = max(max(mx * nums[i], nums[i]), mn * nums[i])
            min_here = min(min(mx * nums[i], nums[i]), mn * nums[i])
            max_so_far = max(max_here, max_so_far)
        return max_so_far

# T: O(a)
# S: O(1)