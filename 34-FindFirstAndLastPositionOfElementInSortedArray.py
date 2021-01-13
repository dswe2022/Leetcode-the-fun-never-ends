# Leetcode 34. Find First and Last Position of Element in Sorted Array
# Medium 1/2/21


# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

 

# Constraints:

#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     nums is a non-decreasing array.
#     -109 <= target <= 109

# Approach 1: Linear Scan

# Intuition

# Checking every index for target exhausts the search space, so it must work.

# Algorithm

# First, we do a linear scan of nums from the left, breaking when we find an instance of target. If we never break, then target is not present, so we can return the "error code" of [-1, -1] early. Given that we did find a valid left index, we can do a second linear scan, but this time from the right. In this case, the first instance of target encountered will be the rightmost one (and because a leftmost one exists, 
# there is guaranteed to also be a rightmost one). We then simply return a list containing the two located indices.


# Solution 1
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]        




# Time complexity : O(n)O(n)O(n)
# This brute-force approach examines each of
# the n elements of nums exactly twice, so the overall runtime is linear.
# Space complexity : O(1)O(1)O(1)
# The linear scan method allocates a fixed-size array and a few integers, 
# so it has a constant-size memory footprint.







# Solution 2

# Intuition

# Because the array is sorted, we can use binary search to locate the left and rightmost indices.

# Algorithm

# The overall algorithm works fairly similarly to the linear scan approach, except for the 
# subroutine used to find the left and rightmost indices themselves. Here, we use a modified binary 
# search to search a sorted array, with a few minor adjustments. First, because we are locating the 
# leftmost (or rightmost) index containing target (rather than returning true iff we find target), the 
# algorithm does not terminate as soon as we find a match. Instead, we continue to search until lo == hi and 
# they contain some index at which target can be found.

# The other change is the introduction of the left parameter, which is a boolean indicating what to do in the 
# event that target == nums[mid]; if left is true, then we "recurse" on the left subarray on ties. Otherwise, 
# we go right. To see why this is correct, consider the situation where we find target at index i. The leftmost 
# target cannot occur at any index greater than i, so we never need to consider the right subarray. The same 
# argument applies to the rightmost index.

# The first animation below shows the process for finding the leftmost index, and the second shows the process 
# for finding the index right of the rightmost index.

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]





    # Time complexity : O(log⁡N)\mathcal{O}(\log N)O(logN)

    # Here we invoke binary search twice. Let's compute time complexity with the help of master theorem T(N)=aT(Nb)+Θ(Nd)T(N) = aT\left(\frac{N}{b}\right) + \Theta(N^d)T(N)=aT(bN​)+Θ(Nd). The equation represents dividing the problem up into aaa subproblems of size Nb\frac{N}{b}bN​ in Θ(Nd)\Theta(N^d)Θ(Nd) time. Here at step there is only one subproblem a = 1, its size is a half of the initial problem b = 2, and all this happens in a constant time d = 0. That means that log⁡ba=d\log_b{a} = dlogb​a=d and hence we're dealing with case 2 that results in O(nlog⁡balog⁡d+1N)\mathcal{O}(n^{\log_b{a}} \log^{d + 1} N)O(nlogb​alogd+1N) = O(log⁡N)\mathcal{O}(\log N)O(logN) time complexity.

    # Space complexity : O(1)\mathcal{O}(1)O(1)

    # All work is done in place, so the overall memory usage is constant.
