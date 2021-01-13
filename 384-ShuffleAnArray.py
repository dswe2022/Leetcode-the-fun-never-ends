# Leetcode 384. Shuffle an Array
# Medium 12/29/20

# Given an integer array nums, design an algorithm to randomly shuffle the array.

# Implement the Solution class:

#     Solution(int[] nums) Initializes the object with the integer array nums.
#     int[] reset() Resets the array to its original configuration and returns it.
#     int[] shuffle() Returns a random shuffling of the array.

 

# Example 1:

# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]




import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.origin = list(nums)
        self.curr = list(nums)
        self.size = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.curr = list(self.origin)
        return self.curr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(self.size):
            pos = random.randint(0, i)
            # swap i and pos
            self.curr[i], self.curr[pos] = self.curr[pos], self.curr[i]
        return self.curr
    
    
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()