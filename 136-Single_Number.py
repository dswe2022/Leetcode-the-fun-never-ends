# Leetcode 136 Single Number
# 12/13/20 

# Given a non-empty array of integers nums,
# every element appears twice except for one.
# Find that single one.

# Solution 1
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for a in nums:
            result ^= a
        return result




# Solution 2
# Hash Table approach

# We use hash table to avoid the O(a) time
# requried for searching the element.
# 1.) Iterate through all elements in nums.
# 2.) Try if hash_table hash_table has the key for pop
# 3.) If not, set up key/value pair
# 4.) In the end, there is only one element in hash_table, so use popitem to get it

class Solution(object):
    def singleNUmber(self, nums):
        hash_table = defaultdict(int)
        for a in nums:
            hash_table[a] +=1
        for i in hash_table:
            if hash_table[i] == 1:
                return i



# Solution 3
# List operation
# 1.) Iterate over all the elements in nums
# 2.) If some number in nums is new to array,
# append it
# 3.) If some number is already in the array, remove it.

class Solution(object):
    def singleNUmber(self, nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


#Time: O(a^2), we iterate through nums, taking O(a) time
