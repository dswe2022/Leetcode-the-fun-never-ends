# Leetcode 49. Group Anagrams
# Medium 12/26/20


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Approach 1: Categorize by Sorted String
# Intuition
# Two strings are anagrams if and only if their sorted strings are equal.
# Algorithm
# Maintain a map ans : {String -> List} where each key K\text{K}K is a sorted string, 
# and each value is the list of strings from the initial input that when sorted, are equal to K\text{K}K.

# In Java, we will store the key as a string, eg. code. In Python, we will store the key as a 
# hashable tuple, eg. ('c', 'o', 'd', 'e').


# Solution 1
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


# T: O(a)
# S: O(a), where is the number of elements in defaultdict.




# Time Complexity: O(NKlog⁡K)O(NK
# \log K)O(NKlogK), where NNN is the length of strs, and KKK is the maximum length 
# of a string in strs. The outer loop has complexity O(N)O(N)O(N) as we iterate through each
# string. Then, we sort each string in O(Klog⁡K)O(K \log K)O(KlogK) time.

# Space Complexity: O(NK)O(NK)O(NK), the total information content stored in ans. 