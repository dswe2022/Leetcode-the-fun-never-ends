# Leetcode 215. Kth Largest Element in an Array
# Medium 12/27/20


# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4

# Solution 1

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = sorted(nums, reverse=True)
        return res[k-1]


# T: O(a*log(a))
# S: O(1)


# Solution 2


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        amount = len(nums)
        while amount > k:
            heapq.heappop(nums)
            amount -= 1
        return nums[0]


# T: O(a*log(a))
# S: O(1)
