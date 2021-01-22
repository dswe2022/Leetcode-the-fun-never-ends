# Leetcode 15 3Sum
# Easy 1/21/21 

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

# Follow up to 2 sums problem

# Algorithm

# The implementation is straightforward - we just need to modify twoSumII to produce triplets and skip repeating values.

#     For the main function:
#         Sort the input array nums.
#         Iterate through the array:
#             If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
#             If the current value is the same as the one before, skip it.
#             Otherwise, call twoSumII for the current position i.

#     For twoSumII function:
#         Set the low pointer lo to i + 1, and high pointer hi to the last index.
#         While low pointer is smaller than high:
#             If sum of nums[i] + nums[lo] + nums[hi] is less than zero, increment lo.
#             If sum is greater than zero, decrement hi.
#             Otherwise, we found a triplet:
#                 Add it to the result res.
#                 Decrement hi and increment lo.
#                 Increment lo while the next value is the same as before to avoid duplicates in the result.

#     Return the result res.

# Solution 1 two pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

# T: O(a^2), sorting takes O(alog(a)) O(a^2 + alog(a)) => O(a^2)
# S: O(log(a)) to O(a)

# Solution 2 Hashset

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1


# T: O(a^2)
# S: O(a) for hashset

# Solutino 3 No Sort

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res

# T: O(a^2)
# S: O(a)

