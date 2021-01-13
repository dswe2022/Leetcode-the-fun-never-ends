# Leetcode 371. Sum of Two Integers
# Medium 12/29/20 

# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3

# Example 2:

# Input: a = -2, b = 3
# Output: 1

class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not a:
            return b
        if not b:
            return a

        MAX_INT_32_BITS = 0x7FFFFFFF
        MASK_32_BITS = 0xFFFFFFFF

        while b:
            # a & b will find out all positions at where a and b both have '1', 
            # and these '1's will become carry.
            carry = (a & b) & MASK_32_BITS

            # a ^ b will find out all positions at where a and b have different bit, 
            # at these positions, either '1' belongs to a or '1' belongs to b,
            # then we assign all these bits to a
            a = (a ^ b) & MASK_32_BITS

            # we shift all bits in carrys to left by one position (make them bigger)
            # to be ready to add back to a in next round.
            b = (carry << 1) & MASK_32_BITS

            # each time we check b, if b become to 0, which means there is no carry, 
            # so we can stop.

        if a <= MAX_INT_32_BITS:
            return a
        else:
            # Because we mask a as a 32 bits int, and a has been greater than MAX_INT_32_BITS,
            # which means now a is a negative number, based on the "two's complement", 
            # the highest significant digits should be all '1's.
            # And we can image now a's 32th bit (from right to left) must be '1', because a now is a negative int.
            # But in Python there are more than 32 bits, so we also need to make all high significant bits to be '1'.
            # So first we use '~0' to get all '1's, then we shift it to left 32 times, making it has 32 '0's at right side,
            # something like '111111111111...1110000000...000', then we make it do 'OR' with a, 
            # to left all bits on the left side of a to be '1's, to build a real Python negative int.
            return (~0 << 32) | a




# Revelation:

#     In Python, the integer is not 32 bits.
#     which means, if x is a positive int, -x = (~x) + 1. For example, we have 3, and -3 should be (~3) + 1.
#     One hex digit stands for 4 binary bits, such as 0xF (in hex) means 1111 (in binary).
#     Max int in 32-bits int is 0x7FFFFFFF.
#     Min int in 32-bits int is ~0x7FFFFFF.
#     32 bits mask is 0xFFFFFFFF.
#     num1 & num2, will get all the '1's at where num1 and num2 both has '1's, which can be used as the carry 
#     in the calculation.

#     num1 ^ num2, will get all the '1's at where num1 and num2 has different bits, either num1 at this position has
#     '1' or num2 at this position has '1'. Think about why we do 'a = a ^ b', because we have store the carry, and 
#     if at the position a and b all have '1's, which will be '0' in the result, and carry will be '1', and carry 
#     will be shift to left by one position, then added to the next round calculation.

# Note:

#     Time complexity = O(32) = O(1), because the worst case is each time there is some carry, and if the carry is 
#     not 0, we must keep doing the calculation (while loop), and there are at most 32 bits need to be calculated,
#     so T = O(32) = O(1).
