# Leetcode 242 Valid Anagram
# Easy 12/13/20 

class Solution(object):
    def isAnagram(self,s, t):
        hm = {}
        for a in s:
            if a not in hm:
                hm[a] - 1
            else:
                hm[a] +=1
        for b in t: 
            if b in hm:
                hm[b] -= 1
            else:
                hm[b] = 1
        
        return True if all(v == 0 for v in hm.values()) else False


# Time: O(a), a is number of characters
# Space: O(1), given we are talking about English language
# there are only 26 letters. The number of key:value pairs stops at most
# 26 for an English word. 

