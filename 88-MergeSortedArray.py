# Leetcode 88 Merge Sorted Array
# Easy 12/25/20

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[0:m]+nums2[0:n])
        return nums1[:]



# Time: O(a*log(a)), a is number of elments total which is m+n
# Space: O(1), no additional space because algorithm merges into nums1 array.


