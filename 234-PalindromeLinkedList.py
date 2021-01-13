# Leetcode 234 Given a singly linked list, determine if it is a palindrome.
# Easy 12/25/20

# Given a singly linked list, determine if it is a palindrome.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        slow = reverseList(slow)

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True

# T: O(a), where a is number of elements in linked list.
# S: O(1), constant space. Other than pointer, no other data structures are used.
