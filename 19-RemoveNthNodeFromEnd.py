# Leetcode 19 Remove Nth Node From End of List
# Medium 1/5/21

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:

# Input: head = [1], n = 1
# Output: []

# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

 

# Constraints:

#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        front=head
        back = head
        counter = 0
        flag = False
        while counter<=n:
            if(not front):
                flag = True
                break
            front = front.next
            counter+=1
        while front:
            front = front.next
            back = back.next
        if not flag:
            temp = back.next
            back.next = temp.next
            temp.next = None
        else:
            head = head.next
        return head        