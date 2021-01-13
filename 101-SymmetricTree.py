# Leetcode 101 Symmetric Tree
# Easy 12/18/20

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Solution 1 
# Recursive Solution
class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
        

# Time: O(a)
# Space: O(1)



# Solution 2
# Iterative Solution
 
from collections import deque

class Solution(object):
    def isSymmetric(self,root):
        q = deque()
        q.append(root)
        q.append(root)
        while not len(q) == 0:
            t1 =  q.popleft()
            t2 =  q.popleft()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            
            if t1.val != t2.val:
                return False
            
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        
        return True

# Time: O(a)
# Space: O(a)