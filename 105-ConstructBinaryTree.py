# Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium 12/29/20 

# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Solution 1
# Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTree(preSt, preEnd, inSt, inEnd, indt, preorder):
            if preSt > preEnd or inSt > inEnd: return 
            root = TreeNode(preorder[preSt])
            index = indt[root.val]
            offset = index - inSt   #the amount of node in current left subtree.
            root.left = buildTree(preSt+1, preSt+offset, inSt, index-1, indt, preorder)
            root.right = buildTree(preSt+offset+1, preEnd, index+1, inEnd, indt, preorder)
            return root
        
        indt = {v: i for i, v in enumerate(inorder)}
        return buildTree(0, len(preorder)-1, 0, len(inorder)-1, indt, preorder)


# T: O(a)
# S: O(a)



# Solution 2A
# Pop preorder as Root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder: 
            return 
        rootval = preorder.pop(0)
        rootind = inorder.index(rootval)
        root = TreeNode(rootval)
        root.left = self.buildTree(preorder, inorder[:rootind])
        root.right = self.buildTree(preorder, inorder[rootind+1:])
        return root


# T: O(a*a)
# S: O(1)


# Solution 2B
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preiter, dt, st, end):
            if st > end: return
            rootval = next(preiter)
            rootind = dt[rootval]
            root = TreeNode(rootval)
            root.left = build(preiter, dt, st, rootind-1)
            root.right = build(preiter, dt, rootind+1, end)
            return root
        
        dt = {v: i for i, v in enumerate(inorder)}
        iterpre = iter(preorder)
        return build(iterpre, dt, 0, len(inorder)-1)

# T: O(a)
# S: O(a)



# Solution 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return 
        root = TreeNode(preorder[0])
        stack, j = [root], 0  #j is the index of inorder
        for i in range(1, len(preorder)):  
            if stack[-1].val != inorder[j]:  #the coming node is left subtree (child)
                node = TreeNode(preorder[i])
                stack[-1].left = node
                stack.append(node)
            else:  
            	#left sub tree established, pop out all of them except the last root node
                while stack and stack[-1].val == inorder[j]: 
                    par = stack.pop(); j += 1
                #the last node as the parent of coming right child.
                node = TreeNode(preorder[i])
                par.right = node
                stack.append(node)
        return root


# T: O(1)
# S: O(a)

