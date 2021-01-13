# Leetcode 148. Sort List
# Medium 12/29/20 

# Given the head of a linked list, return the list after sorting it in ascending order.
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []

# Constraints:

#     The number of nodes in the list is in the range [0, 5 * 104].
#     -105 <= Node.val <= 105




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1, l2):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val > l2.val: l1, l2 = l2, l1
                tail.next = l1
                l1 = l1.next
                tail = tail.next
                tail.next = l1 if l1 else l2
            return dummy.next
        if not head or not head.next: 
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return merge(self.sortList(head), self.sortList(mid))

# T: O(a)
# S: O(a)