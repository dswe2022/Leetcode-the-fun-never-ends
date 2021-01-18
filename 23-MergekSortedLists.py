# Leetcode 23. Merge k Sorted Lists
# Hard 1/16/21

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists
# into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

 

# Constraints:

#     k == lists.length
#     0 <= k <= 10^4
#     0 <= lists[i].length <= 500
#     -10^4 <= lists[i][j] <= 10^4
#     lists[i] is sorted in ascending order.
#     The sum of lists[i].length won't exceed 10^4.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Solution 1 Brute force

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)

        for l in lists:
            while l:
                self.nodes.append(l.val)        
                l = l.next
            
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next


        return head.next

# O(alog(a)) where a is the total number of nodes.
# collected all the claues costs O(a) time.
# stable sorteing algroithm costs O(alog(a)) time.
# Iteratring for creating the linked list costs O(a) time

# Space complexity: O(a)
# Sorting cost O(a) space depends on the algorithm you choose.
# Creating a new linked list costs O(a) space.




# Solution 2 Optimize Approach 2 by priority queue
# Almost the same as the one above but optimize the comparison process by priority queue. 

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self,lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val,l))
        while not q.empty():
            val,node = ListNode(val)
            point.next = ListNode(val)
            point = point.next
            node = node.next

            if node:
                q.put((node.val, node))
        return head.next



# T: O(a log(k)), where k is the number of linked lists.
# The comparison cost will be reduced to O(log(k)) for every pop and insertion to 
# priority queue. But finding the node with the smallest value just costs O(1) time.

# There are N nodes in the final linked list.


# Space complexity: O(a) creating a new linked list cost O(a) space.
# O(k), the code above present applies in-place method which cost O(1) space.
# The priority queue (often implemented with heaps) costs O(k) space (it's far less than a in most situations).


# Solution 3: Merge lists one by one.
# Convert merge k lists problem to merge 2 lists (k-1) times. here is the merge 2 lists problem page.

# Time complexity: O(kA) where k is the number of linked list.
# We can merge two sorted linked list in O(a) time where a is the total number of nodes in two lists.
# Sum up the merge process and we can get: O(ka).

# Space complexity: O(1), we can merge two sorted linked list O(1) space.



# Solution 5: Merge with Divide and Conquer
# Intuition & algorithm
# This approach walks alongside the one above but is improved a lot. We don't need to traverse most nodes many times repeatedly.
# Pair up k lists and merge each pair.

class Solution(object):
    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else None


    
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        

        if not l1:
            point.next = l2
        else:
            point.next = l1

        return head.next



# T: O(a log(k)), where k is the number of linked lists.
# S: O(1), we can merge two sorted linked lists in O(1) space.



