# Leetcode 163. Missing Ranges
# Easy 12/26/20 



# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

# Thought process:

# Get missing range from lower to nums[0].
# Get missing ranges in nums.
# Get missing range from nums[len - 1] to upper.


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        newLower = lower - 1
        newUpper = upper + 1
        tmpLow = newLower
        res = []

        for i in range(len(nums)):
            if nums[i] - tmpLow > 1:
                res.append(self.get_range(tmpLow + 1, nums[i] - 1))
            tmpLow = nums[i]

        if newUpper - tmpLow > 1:
            res.append(self.get_range(tmpLow + 1, newUpper - 1))

        return res

    def get_range(self, lower, upper):
        if lower == upper:
            return str(lower)
        else:
            return str(lower) + '->' + str(upper)