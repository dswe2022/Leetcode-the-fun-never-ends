# Leetcode 104 Maximum Depth of Binary Tree
# 12/13/20 
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path 
# from the root node down to the farhest leaf node.


class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max( self.maxDepth(root.left) , self.maxDepth(root.right))



# Time: O(h), h is height of tree.
# Space: O(1) constant memory