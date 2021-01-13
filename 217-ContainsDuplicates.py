# Leetcode 217 Contains Duplicates
# Easy 12/13/20 

class Solution(object):
    def containsDuplicate(self, nums):
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
            
        return False


# Time: O(a), a is number of elements in array.
# Space: O(a), a is number of elements in set