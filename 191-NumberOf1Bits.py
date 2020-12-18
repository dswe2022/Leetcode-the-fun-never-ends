# Leetcode 191 Number of 1 Bits
# Easy 12/18/20


# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
# Note:
# Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above, the input represents the signed integer. -3.
# Follow up: If this function is called many times, how would you optimize it?

# Solution 1
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


# Time: O(1)
# Space: O(1)



# Solution 2
def hammingWeight(n):
    count = 0
    while n:
        count += n&1
        n >>= 1
    return count

# Time: O(1)
# Space: O(1)

# Solution 3
def hammingWeight(n):
    count = 0
    while n:
        count +=1
        n &=n -1
    return count # This operation can turn the lowest 1 on into 0.

