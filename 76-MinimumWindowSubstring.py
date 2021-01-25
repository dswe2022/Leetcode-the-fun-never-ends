# Leetcode 76. Minimum Window Substring
# Hard 1/24/21

# Given two strings s and t, return the minimum window in s which will contain
# all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
 

# Constraints:

# 1 <= s.length, t.length <= 105
# s and t consist of English letters.

# Solution 1
# Window solution

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# Solution 2
# Optimized solution 



class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        dict_t = Counter(t)

        required = len(dict_t)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    

            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


# T: O(|S|+|T|) where |S| and |T| represent the lengths of strings S and T. 
# S: O(|S| + |T|)


# Solution 3

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t: return ""
        t_table = Counter(list(t))
        hash_table = defaultdict(int)
        value_list = []
        result = ""
        low = -1

        for i in range(len(s)):
            if s[i] in t:
                if s[i] in t_table:
                    hash_table[s[i]] += 1
                value_list.append([i, s[i]])
                if self.check_table(t_table, hash_table):
                    if low == -1: low = value_list.pop(0)[0]
                    sub = s[low:i + 1]
                    if len(sub) < len(result) or result == "":
                        result = sub
                    while True:
                        if len(value_list) > 0:
                            hash_table[s[low]] -= 1
                            low = value_list.pop(0)[0]
                        else: break
                        if not self.check_table(t_table, hash_table): break
                        sub = s[low:i + 1]
                        if len(sub) < len(result) or result == "":
                            result = sub
        return result

    def check_table(self, t_table, hash_table):
        for item in t_table:
            if t_table[item] > hash_table[item]: return False
        return True