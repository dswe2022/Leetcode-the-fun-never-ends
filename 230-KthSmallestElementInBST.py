# Leetcode 230. Kth Smallest Element in a BST
# Medium 12/26/20

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -=1
            if k == 0:
                break
            root = root.right
        return root.val

# T: O(a^2)
# S: O(a)