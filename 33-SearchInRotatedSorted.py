# Leetcode 33 Search in Rotated Sorted Array
# Medium 1/5/21

# You are given an integer array nums sorted in 
# ascending order (with distinct values), and an integer target.
# Suppose that nums is rotated at some pivot unknown to you 
# beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# If target is found in the array return its index, otherwise, return -1.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# Constraints:

#     1 <= nums.length <= 5000
#     -104 <= nums[i] <= 104
#     All values of nums are unique.
#     nums is guaranteed to be rotated at some pivot.
#     -104 <= target <= 104


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Did not find the target
        if begin > end:     
            return -1
        mid = (begin + end) // 2
        if A[begin] < A[end]:   
            rotated = False # Sorted and not rotated
        else:                   
            rotated = True  # Sorted and then rotated
        if A[mid] == target:
            # Target found
            return mid
        elif A[mid] < target:
            # If array is not rotated, no need to search in the left part
            if rotated:
                # Target might be in the left part
                temp = self._searchHelper(A, target, begin, mid - 1)
                if temp != -1:  return temp
            # Search in the right part
            return self._searchHelper(A, target, mid + 1, end)
        else:
            # If array is not rotated, no need to search in the right part
            if rotated:
                # Target might be in the right part
                temp = self._searchHelper(A, target, mid + 1, end)
                if temp != -1:  return temp
            # Search in the left part
            return self._searchHelper(A, target, begin, mid - 1)
