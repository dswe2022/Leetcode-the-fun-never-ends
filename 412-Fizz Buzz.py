# Leetcode 412 Fizz Buzz 
# Easy 12/13/20

# Write a problem that outputs the 
# But for multiples of three it should output "Fizz" instead 
# of the number and for the multiples of five output "Buzz".
# For numbers which are multiples of both three
# and five output "FizzBuzz".

# Approach 1: Naive Approach
# The moment you hear of FizzBuzz you think whether the number is divisible 
# by 3,5 , or both.

# Algorithm: 
# 1.) Initialize an empty answer list.
# 2.) Iterate on the numbners from 1...N
# 3.) For every number, if it is divisible by both 3 and 5, add fizzbuzz
# 4.) Else, check if the number
# 5.) Else, add the number.


# Naive Solution 1
class Solution:
    def fizzBuzz(self, n):
        ans = []
        for num in range(1, n + 1):
            divisible_by_3 = (num%3 == 0)
            divisible_by_5 = (num%5 == 0)
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))
        return ans`




# Time: O(a)
# Space: O(1)

# FizzBuzz Solution 2
# String Concatenation this approach won't reduce the asymptoitc complexity,
# but proves to be a neater solution when FizzBuzz
# comes with a twist. What if FizzBuzz is now.

class Solution(object):
    def fizzBuzz(self,n):
        ans = []
        for num in range(1, n+1):
            divisible_by_3 = (num%3 == 0)
            divisible_by_5 = (num%5 == 0)
            num_ans_str = ""

            if divisible_by_3:
                num_ans_str += "Fizz"

            if divisible_by_5:
                num_ans_str += "Buzz"
            
            if not num_ans_str:
                num_ans_str = str(num)

            ans.append(num_ans_str)

        return ans


# Time: O(a)
# Space: O(1)



