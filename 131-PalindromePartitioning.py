# Leetcode 131. Palindrome Partitioning
# Medium 12/29/20 

# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:

# Input: s = "a"
# Output: [["a"]]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        self.result = []
        self.end = len(s)
        self.str = s

        self.is_palindrome = [[False for i in range(self.end)]
                              for j in range(self.end)]

        for i in range(self.end-1, -1, -1):
            for j in range(self.end):
                if i > j:
                    pass
                elif j-i < 2 and s[i] == s[j]:
                    self.is_palindrome[i][j] = True
                elif self.is_palindrome[i+1][j-1] and s[i] == s[j]:
                    self.is_palindrome[i][j] = True
                else:
                    self.is_palindrome[i][j] = False

        self.palindrome_partition(0, [])
        return self.result

    def palindrome_partition(self, start, sub_strs):
        if start == self.end:
            # It's confused the following sentence doesn't work.
            # self.result.append(sub_strs)
            self.result.append(sub_strs[:])
            return

        for i in range(start, self.end):
            if self.is_palindrome[start][i]:
                sub_strs.append(self.str[start:i+1])
                self.palindrome_partition(i+1, sub_strs)
                sub_strs.pop()      # Backtracking here

# T: O(a*a)
# S: O(a)

