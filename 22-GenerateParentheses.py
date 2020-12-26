# Leetcode 22. Generate Parentheses 
# Medium 12/26/20

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



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