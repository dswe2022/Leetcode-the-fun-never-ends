# Leetcode 103. Binary Tree Zigzag Level Order Traversal
# Medium 12/29/20 

# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its zigzag level order traversal as:

# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = [root]
        reverse = False
        while q:
            new_q = []
            if reverse:
                res.append([n.val for n in q][::-1])
            else:
                res.append([n.val for n in q])
            reverse = not reverse
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return res

# T: O(a*a)
# S: O(a)