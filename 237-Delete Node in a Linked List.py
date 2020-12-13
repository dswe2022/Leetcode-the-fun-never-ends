# Leetcode 237 Delete Node in a Linked list
# 12/14/20 

# Approach: swap with next Node.
# The usual way of deleting a node from a Linked List
# is to modify the next pointer of the node before it
# to point to the node after it.

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next



