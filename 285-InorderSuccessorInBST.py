# Leetcode 	285	Inorder Successor in BST    
# Medium 1/1/21

# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# Note: If the given node has no in-order successor in the tree, return null.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None

        while root != None and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        if root == None:
            return None

        if root.right == None:
            return successor


        root = root.right
        while root.left != None:
            root = root.left
        return root

# T: O(a)
# S: O(1)