# Leetcode 146. LRU Cache

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# Follow up:
# Could you do get and put in O(1) time complexity?

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

 

# Constraints:

#     1 <= capacity <= 3000
#     0 <= key <= 3000
#     0 <= value <= 104
#     At most 3 * 104 calls will be made to get and put.


# We're asked to implement the structure which provides the following operations in O(1)\mathcal{O}(1)O(1) time :

#     Get the key / Check if the key exists

#     Put the key

#     Delete the first added key

# The first two operations in O(1)\mathcal{O}(1)O(1) time are provided by the standard hashmap, and the last one - by linked list.

# We are asked to implemtn the structure which provides the following operations in O(1) time.

# Get the key/check if the key exists
# Put the key
# Delete the first added key

# Solution 1
# Use a OrderedDict from collections.

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        # Type capacity: int
        self.capacity = capacity
    
    def get(self,key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)

# T: O(1) both for put and get since all operations with ordered dictionary: get/in, 
# /set/move_to_end/popitem (get/containsKey/put/remove) are done in constant time.

# S: O(capacity).


# Solution 2
# Use a hashmap and Doubly linked list.
# classic solution


# IMPORTANT: The reason why double linked list is used is that the node can remove itself without other reference. 

# It takes constant time to add and remove nodes from the head or tail.
# One particularity about the double linked list implemented here is that there are pseudo head and pseudo tail to 
# mark the boundary.



# Declare the doubly linked list node first.
class DLinkedNode():
    def __init__(self):
        self.key = 0 
        self.value = 0
        self.prev = None
        self.next = None
    

class LRUCache():
    def _add_node(self,node):
        # Always add the new node right after head.
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self.node):
        # Remove an exisiting node from the linked list.
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev


    def _move_to_head(self, node):
        # Move certain node in between to the head.
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # Pop the current tail
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self,capacity):
        # type capacity: int
        self.cache = {}
        self.size = 0
        self.capcity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        # type key: int
        # return type: int
        node = self.cache.get(key, None)
        if not node:
            return -1
        
        # move the accessed node to the head
        self._move_to_head(node)

        return node.value

    def put(self,key, value):
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail 
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value
            node.value = value
            self._move_to_head(node)



# T: O(1)
# S: O(capacity)


# Solution 3

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.queue = []
        

    def updateQueue(self,key):
        self.queue.remove(key)
        self.queue.insert(0,key)
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.updateQueue(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not key or not value:
            return None
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.queue) == self.capacity:
            del self.cache[self.queue.pop(-1)]
        
        self.cache[key] = value
        self.queue.insert(0,key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)