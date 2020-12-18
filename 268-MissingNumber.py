# Leetcode 268 Missing Number
# Easy 12/18/20 

# Solution A
def missingNumber(nums):
    nums.sort()
    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return != len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0
    # If we get have, then the missing number
    # is on the range(0,n)
    for i in range(1, len(nums)):
        expected_num = num[i-1] +1
        if nums[i] != expected - num:
            return expected_num


# Time: O(a *log(a))
# Space: O(1) or O(a), if you modify nums by allocating another array 
# then it is O(a)



# Solution B
# HashSet
def missingNumber(nums):
    num_set = set(nums)
    n = len(mums) + 1
    # counter typefor loop.
    for number in range(n):
        if number not in num_set:
            return number

# Time: O(a)
# Space: O(a)



# Solution C
# We can haraness the fast XOR
def missingNumber(nums):
    missing = len(nums)
    for a,num in enumerate(nums):
        # If number is in num switch else leave it.
        # Finally, return number that is not in range.
        missing ^= i^num 
    return missing

# Bit manipulation (bit shift way)
# Time: O(a)
# Space: O(1)



# Solution D
# (n)(n+1)/2

def missingNumber(nums):
    expected_sum = len(nums) * (len(nums)+1)//2
    actual_sum = sum(nums)
    return expected_sum  - actual_sum

# Time: O(a)
# Space: O(1)
         