# Leetcode 116. Populating Next Right Pointers in Each Node
# Medium 12/29/20 

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
# The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer 
# should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Follow up:

#     You may only use constant extra space.
#     Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

 

# Example 1:

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer 
# to point to its next right node, just like in Figure B. The serialized output is in level order as connected 
# by the next pointers, with '#' signifying the end of each level.

 

# Constraints:

#     The number of nodes in the given tree is less than 4096.
#     -1000 <= node.val <= 1000



# https://gchan2.hatenablog.com/entry/2020/08/16/211826


# Solution 1
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root 
        
        q = collections.deque([])
        q.append(root)
        
        while q:
            qlen = len(q)
            
            for i in range(qlen):
                e = q.popleft()
                
                if i < qlen-1:
                    e.next = q[0]  
                
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
                    
        return root

# T: O(a*a)
# S: O(a)


# Solution 2

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        if root.left:
            root.left.next = root.right
            
            if root.next:
                root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root

# T: O(a)
# S: O(a)


