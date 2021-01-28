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

# Solution 1 Binary Search
# Fina a rotation index rotation_index index of the smallest element in the array. 
# Binary Search works just perfect here.

# Rotation_index splits array in two parts. Compare nums[0] and targte to identify
# in which part one has to look for target.

# Perform binary search in the chosen part of the array.


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)

# T: O(log(a))
# S: O(1)






# Solution 2 One-pass Binary Search
# Instead of going through the input array in two passes, we could achieve the goal in one pass
# with an revised binary search.

# The idea is that we add some additional condition checks in the normal binary search in order
# to better narrow down the scope of the search.

# Initiate the pointer start to 0, and the pointer end to n-1.
# Perform standard binary search. Whilte start <= end.
# Take an index in the middle mid as a pivot.
# If nums[mid] == traget, the job is done, return mid.
# Now there could be two situations:
# Pivot element is larger than the first element in the array. 



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

# T: O(log(a))
# S: O(1)


