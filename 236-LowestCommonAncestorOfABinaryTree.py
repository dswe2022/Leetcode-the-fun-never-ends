# Leetcode 236 Lowest Common Ancestor of a Binary Tree
# Medium 12/17/20 

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in 
# T that has both p and q as descendants (where we allow a node to be descendant of itself)"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1 Recursion

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if any((not root, root == p, root == q)): return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if not l or not r: return l if l else r
        return root


# Space complexity: O(h)

# For a given root, recursively call LCA(root.left, p, q) and LCA(root.right, p, q)

# if both returns a valid node which means p, q are in different subtrees, then root will be their LCA.

# if only one valid node returns, which means p, q are in the same subtree, return that valid node as their LCA.





# Solution 2 

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parent = {root:None}
        stack = [root]

        while (p not in parent) or (q not in parent):
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q


    # Time: 3*O(a)=> O(a) a is number of nodes needed to traverse to p and q.
    # Space: 2*O(a) needs a hashmap and list => which reduces to O(a).