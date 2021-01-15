# Leetcode 226. Invert Binary Tree
# Easy 1/15/21

# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Trivia:
# This problem was inspired by this original tweet by Max Howell:

#     Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


# Solution 1 Fast 12 ms

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root or not (root.left or root.right): return root
        
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root

# Solution 2 Recursive

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

# Solution 3

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))	#left = root.right and right = root.left


