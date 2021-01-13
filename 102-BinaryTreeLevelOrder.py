# Leetcode 102. Binary Tree Level Order Traversal

# Medium 12/27/20 

# Given a binary tree, return the level order 
# traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its level order traversal as:

# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            currLevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                currLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(currLevel)

        return ans


# T: O(a^2)
# S: O(a)