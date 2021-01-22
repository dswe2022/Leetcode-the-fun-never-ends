# Leetcode 12. Integer to Roman
# Medium 1/21/21 

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral.

 

# Example 1:

# Input: num = 3
# Output: "III"

# Example 2:

# Input: num = 4
# Output: "IV"

# Example 3:

# Input: num = 9
# Output: "IX"

# Example 4:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 5:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 

# Constraints:

#     1 <= num <= 3999



# Solution 1 Greedy Approach (Use this)

digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def intToRoman(self, num: int) -> str:
    roman_digits = []
    # Loop through each symbol.
    for value, symbol in digits:
        # We don't want to continue looping if we're done.
        if num == 0: break
        count, num = divmod(num, value)
        # Append "count" copies of "symbol" to roman_digits.
        roman_digits.append(symbol * count)
    return "".join(roman_digits)

# T: O(1), finite set of roman numerals, there is a hard upper limit on how many times the loop can interate.
# This upper limit is 15 times and it occurs for the number 3000, which is representation of MMMDCCCLXXXVIII. 
# Thus time is O(1)

# Space complexity: O(1) the amount of memoryused does not change with the size of the input integer, and is therefore constant.






# Solution 2 # Very fast

def intToRoman(self, num: int) -> str:
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]

# An integer's decimal representation can be treated independently when converting the integer into a Roman Numeral. Notice taht all of the symbols 
# can be split into groups based on their highest factor out of 1000, 100, 10, and 1.

# Getting each digit.

# thousands_digit = integer/1000
# hundreds_digit = (integer % 1000) / 100
# tens_digit = (integer %100) /10
# ones_digit = integer % 10


# The cleanest way is to have 4 separate arrays one for each place value. 

# T: O(1)
# S: O(1)