# Leetcode 22. Generate Parentheses 
# Medium 12/26/20

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

 

# Constraints:

#     1 <= n <= 8


# Solution 1
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def gen(o,c,s):
            if o > c: 
                return
            if o == 0 and c == 0:
                ans.append(s)
                return
            if o == 0:
                gen(o,c-1,s+")")
            else:
                gen(o-1,c,s+"(")
                gen(o,c-1,s+")")
        gen(n,n,"")
        return ans

    # T: O(a)
    # S: O(a)


# Solution 2


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.gen(n,n,"")
        
        return self.ans


    def gen(self, o,c,s):
        if o> c:
            return
        if o == 0 and c == 0:
            self.ans.append(s)
            return
        if o == 0:
            self.gen(o, c-1, s+")")
        else:
            self.gen(o-1, c, s+"(")
            self.gen(o,c-1,s+")")
        
        