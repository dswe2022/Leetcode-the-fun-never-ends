# Leetcode 395. Longest Substring with At Least K Repeating Characters
# Medium 12/31/20

# Given a string s and an integer k, return the length of the longest substring of s such that 
# the frequency of each character in this substring is greater than or equal to k.

 

# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

# Example 2:

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of only lowercase English letters.
#     1 <= k <= 105



class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cache = [collections.Counter()] # cache[i] = Counter(s[:i])
        for i, c in enumerate(s):
            newCounter = copy.copy(cache[-1])
            newCounter[c] += 1
            cache.append(newCounter)
         
        def dfs(lo, hi):
            if hi - lo < k:
                return 0
            counter = cache[hi] - cache[lo]
            sep = set(filter(lambda c: counter[c] < k, counter))
            if sep:
                res = 0
                i = lo
            else:
                return hi - lo
            for j in range(lo, hi):
                if s[j] in sep:
                    res = max(res, dfs(i, j))
                    i = j + 1
            else:
                res = max(res, dfs(i, hi))
            return res
         
        return dfs(0, len(s))

# T: O(a)
# S: O(a), a for the dictionary counter space.