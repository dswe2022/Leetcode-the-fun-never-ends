# Leetcode 328 Odd Even Linked List
# Easy 12/22/20 


# Given a singly linked list, group all odd nodes together 
# followed by the even nodes. Please note here we are talking 
# about the node number and not the value in the nodes.

# You should try to do it in place. The program should run 
# in O(1) space complexity and O(nodes) time complexity.

class Solution(object):
    def oddEventList(self,head):
        if head:
            odd_tail = headcur = head.next
            while cur and cur.next:
                even_head = odd_tail.next
                odd_tail.next = cur.next
                odd_tail = odd_tail.next
                cur.next = odd_tail.next
                odd_tail.next = even_head
                cur = cur.next
        return head

# Time: O(a), a is number of nodes in linked list.
# Space: O(1)

