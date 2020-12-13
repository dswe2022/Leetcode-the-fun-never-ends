# Leetcode 21 Merge Two Sorted Lists
# Easy 12/13/20 

class Node(val):
    def __init__(self,val):
        self._val = val
        self._next = None


class Solution(object):
    def mergeTwoLists(self,L1,L2):
        if not L1 or not L2:
            return L1 or L2
        head = cur
        cur = ListNode(0)
        while L1 and L2:
            if L2.val > L1.val:
                cur.next = L1
                L1 = L1.next
            else:
                cur.next = L2
                L2 = L2.next
                cur - cur.next
        cur.next = L1 or L2
        return head.next


# Time: O(a)
# Space: O(1)


