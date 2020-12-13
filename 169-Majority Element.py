# Leetcode 169 Majority Element 
# Easy 12/13/20 

# Given size n, find the majority element.
# The majority element is the element that 
# appears more than [n/2]  floor down.


# Solution 1: Brute Force
# The brute force uses an algrothm where you iterate through the array for each number to 
# count its occurrences. As soon as a number is found to have appeared, return it.

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num


# Time: O(n^2) -> O(n^2)
# The Brute force algorithm contains two nested
# for loops that each run for n iterations, adding
# up to quadratic time complexity.

# Space: O(1)
# The brute force solution does not allocate additional space 
# proportional to the input size.





# Solution 2: HashMap
# Intuition: we know that the majority element occurs
# more than [n/2] times, and a HashMap allows 
# us to count element occurrences efficiently.


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)

# Time: O(a), we iterate over nums once and male a construct time
# hashmap
# Space: O(b), at most, the hash map can contain n-[n/s] assocations,
# so it occupies O(n) space.



# Solution 3: Sorting
# If the elements are sorted in monotonically increasing (or decreasing) order,
# the majority element can be found at index [n/2] and [n/2]+1, even if n is even.

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) //2]


# Time: O(a * log(a))
# Space: O(1), O(a), if sort in place, O(1), O(a)





# Solution 4: Randomization
# Beacause more than [n/2] array indices are occupied by the majority element, a random
# array index is likely contain the majority element.

# Algorithm: Because a given index is likely to have the majority element, we can just select a 
# random index, check whether its value is the majoirty element, return if it si , and repeat if it is not.
# The algorithm is verifiably correct because we ensure that the randomly chosen value is the majority element before 
# ever returning.


import random
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) //2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


# Time: O(infinity)                
# Space converges: O(1)



# Solution 5: Divide and Conquer
# Intuition: If we know the majority element in the left and right halves of an array, we can determine
# which is the global majority element in linear time.

# Algorithm: Here we apply a classical divide and conquer approach that recurses on the left and right halves
# of an array until an answer can be trivially achieved for a length - 1 array.

# Time: O(a * log(a))
# Space: O(log(a))

class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case: the only element in an array
            # of size 1 is the majority   
            if lo == hi:
                return nums[lo]
            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majoirty_element_rec(lo, mid)
            right = majority_eleemnt_rec(mid _1 ,hi)

            # if the two halves agree on the majority element
            if left == right:
                return left
            # Otherwise, count each element and return the "winner"
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
            return left if left_count > right_count else right
            
        return majority_element_rec(0, len(nums) - 1)



            


