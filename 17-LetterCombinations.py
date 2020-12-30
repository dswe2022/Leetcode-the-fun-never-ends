# Leetcode 17. Letter Combinations of a Phone Number
# Medium 12/29/20 

# Given a string containing digits from 2-9 inclusive, return all possible letter 
# combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.

 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = ""
# Output: []

# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

 

# Constraints:

#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9'].

# Solution 1 DFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
          def dfs(digits, d, l, cur, ans):
            if l == len(digits):
              if l > 0: ans.append("".join(cur))
              return

            for c in d[ord(digits[l]) - ord('0')]:
                cur[l] = c
                dfs(digits, d, l + 1, cur, ans)

          d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
          cur = [' ' for _ in range(len(digits))]
          ans = []
          dfs(digits, d, 0, cur, ans)
          return ans

# T: O(a)
# S: O(a)

# Solution 2 BFS

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      if not digits: return []      
      d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
      ans = [""]
      for digit in digits:
        tmp = []
        for s in ans:
          for c in d[ord(digit) - ord('0')]:
            tmp.append(s + c)
        ans = tmp
      
      return ans

# T: O(a)
# S: O(a)