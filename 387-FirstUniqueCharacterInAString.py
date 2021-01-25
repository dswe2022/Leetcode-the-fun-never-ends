# Leetcode 387 First Unique Character in a String
# Easy 12/18/20 

# Given an a by b 2d grid map of "1" s (land) and "0" (water), return the number of islands.

from collections import Counter

def firstUniqChar(s):
    count = Counter(s)
    #the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    
    return -1


# Time: O(a)
# Space: O(1)


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1