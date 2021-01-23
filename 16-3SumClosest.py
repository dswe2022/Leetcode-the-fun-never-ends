# Leetcode 16. 3Sum Closest
# Medium 1/23/21

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

 

# Constraints:

#     3 <= nums.length <= 10^3
#     -10^3 <= nums[i] <= 10^3
#     -10^4 <= target <= 10^4


# Solution 1
# Check the target for less.
# abs(target - sum) is the distance of diff AKA diff
# abs(diff) 



class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Create a diff 
        diff = float("inf")
        nums.sort()
        for idx in range(len(nums)):
            hi = len(nums)-1
            lo = idx + 1             
            while lo < hi:
                sum = nums[lo] + nums[hi] + nums[idx]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -=1
                if diff == 0:
                    break
        return target - diff 


