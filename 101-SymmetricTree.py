# Leetcode 101 Symmetric Tree
# Easy 12/14/20

class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
        

