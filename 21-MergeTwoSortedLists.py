# Leetcode 21 Merge Two Sorted Lists
# Easy 12/13/20 

# Solution 1
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



# Solution 2

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        head = small = l1 if l1.val < l2.val else l2

        big = l1 if l1.val >= l2.val else l2
        pre = None

        while big:
            if not small:
                pre = small
                small = small.next
            else:
                tmp = big.next
                pre.next = big
                pre = big
                big.next = small
                big - tmp

        return head




# Solution 3

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

            

