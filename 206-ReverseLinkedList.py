# Leetcode 206 Reverse Linked List 
# Easy 12/13/20 

# Reverse Linked List 
# Approach 1: Iterative
# Assume that we have linked list 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive: T O(n),  M O(n)
        
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead



# Time: O(a) assume that a is the list's length, the time complexity is O(a)
# Space: O(1)



# Approach 2 Recursive version is slightly tricker and the key is to work
# work backwards. Assume that the rest of the list had already been reversed, now how do I reverse the front part?

# Assume from node n (k+1) to n (m) had been reversed and you are at node n(k).
# Be very careful that n(1), next must point to 0.
# If you forget about this, your linked list has a cycle it.
# This bug could be caught if you test your code with a linked list of size 2.


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# Time: O(a), assume that a is the list's length, the time complexity is O(a)
# Space: O(a), the extra space comes from implicit stack space due to recursion.
# The recursion could go up to levels deep.


