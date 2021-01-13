# Leetcode 138. Copy List with Random Pointer
# Medium 1/2/21


# Deep Copy

# Deep copy a linked list, means you need to create new nodes 
# (each copy with a new memory address) and linked up all these new 
# nodes corresponding to the relationships of their original copies.
# Random Pointers

# Without “random pointers”, it is really simple problems to duplicate a 
# new linked list. It could be done by duplicating the head node and duplicate 
# the next node nodes, and go on.

# However, with the “random pointers”, the problem is that, when we get a pointer, 
# it is very possible that we have not crate the node which the pointer points to yet. 
# So we cannot deep copy the linked list in one pass. We need to deep copy the linked 
# list without assigning the random pointers in the first pass, and then fill in the 
# random pointers in the second scan of the list. To speed up the second pass, we may
#  need the hash map to store the mapping from original node to its copy.

# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

#     val: an integer representing Node.val
#     random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

# Example 1:

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Example 4:

# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.

 

# Constraints:

#     -10000 <= Node.val <= 10000
#     Node.random is null or pointing to a node in the linked list.
#     The number of nodes will not exceed 1000.



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Modify original structure: Original->Copy->Original->Copy
        # node.next.random = node.random.next
        # O(n) and O(1)
        p = head
        while p is not None:
            next = p.next
            copy = Node(p.val)
            p.next = copy
            copy.next =  next
            p = next
        p = head
        while p is not None:
            if p.random is not None:
                p.next.random = p.random.next
            p = p.next.next
        p = head
        if p is not None:
            headCopy = p.next
        else:
            headCopy = None
        while p is not None:
            copy = p.next
            p.next = copy.next
            p = p.next
            if p is not None:
                copy.next = p.next
        return headCopy

    
# T: O(a)
# S: O(1)