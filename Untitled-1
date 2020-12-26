# Leetcode 94. Binary Tree Inorder Traversal
# Medium 12/26/20
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res+= self.inorderTraversal(root.right)
        return res




# Solution 2

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
        
        
    def helper(self,root,res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right,res)
        


# Solution 3

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root ==None:
            return []
        self.left =self.inorderTraversal(root.left)
        self.right = self.inorderTraversal(root.right)
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)