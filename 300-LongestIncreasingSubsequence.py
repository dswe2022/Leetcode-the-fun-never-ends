# Leetcode 300. Longest Increasing Subsequence
# Medium 12/31/20

# https://medium.com/swlh/a-visual-guide-to-solving-the-longest-increasing-subsequence-problem-dabbee570551

# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without
# changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

#  Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

 

# Constraints:

#     1 <= nums.length <= 2500
#     -104 <= nums[i] <= 104

 

# Follow up:

#     Could you come up with the O(n2) solution?
#     Could you improve it to O(n log(n)) time complexity?


class Solution:
    def lengthOfLIS(self, seq: List[int]) -> int:
        if not seq:
            return seq
        M = [None] * len(seq)   
        P = [None] * len(seq)
        L = 1
        M[0] = 0
        for i in range(1, len(seq)):
            lower = 0
            upper = L
            if seq[M[upper-1]] < seq[i]:
                j = upper
            else:
                while upper - lower > 1:
                    mid = (upper + lower) // 2
                    if seq[M[mid-1]] < seq[i]:
                        lower = mid
                    else:
                        upper = mid
                j = lower    
            P[i] = M[j-1]
            if j == L or seq[i] < seq[M[j]]:
                M[j] = i
                L = max(L, j+1)
        r = []
        pos = M[L-1]
        for _ in range(L):
            r.append(seq[pos])
            pos = P[pos]
        return len(r[::-1])

# T: O(a*b)
# S: O(a)

