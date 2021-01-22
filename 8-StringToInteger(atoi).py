# Leetcode 8. String to Integer (atoi)
# Medium 1/21/21 

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

#     Read in and ignore any leading whitespace.
#     Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
#     Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
#     Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
#     If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
#     Return the integer as the final result.

# Note:

#     Only the space character ' ' is considered a whitespace character.
#     Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

# Example 1:

# Input: str = "42"
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# The parsed integer is 42.
# Since 42 is in the range [-231, 231 - 1], the final result is 42.

# Example 2:

# Input: str = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -42" ("42" is read in)
#                ^
# The parsed integer is -42.
# Since -42 is in the range [-231, 231 - 1], the final result is -42.

# Example 3:

# Input: str = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
#              ^
# The parsed integer is 4193.
# Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

# Example 4:

# Input: str = "words and 987"
# Output: 0
# Explanation:
# Step 1: "words and 987" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
#          ^
# The parsed integer is 0 because no digits were read.
# Since 0 is in the range [-231, 231 - 1], the final result is 4193.

# Example 5:

# Input: str = "-91283472332"
# Output: -2147483648
# Explanation:
# Step 1: "-91283472332" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "-91283472332" ('-' is read, so the result should be negative)
#           ^
# Step 3: "-91283472332" ("91283472332" is read in)
#                      ^
# The parsed integer is -91283472332.
# Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.

# Solution 1

class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(map(str, s.split()))
        
        if len(s) > 0:
            num = 0
            sign = 1
            char = None

            if s[0][0] == "-" or s[0][0] == "+":
                sign = -1 if s[0][0] == "-" else 1
                char = s[0][1:]
            else:
                char = s[0]

            for i in char:
                if i.isdigit():
                    num = num * 10 + int(float(i))
                else:
                    break

            if  num != 0:
                num = num * sign
                if num in range(-2**31, 2**31):
                    return num
                else:
                    return -2**31 if num < 0  else 2**31-1
            else:
                return 0
        
        else:
            return 0




# Solution 2


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ') #strips off the white space from the left
        if s == '' or s == '-' or s == '+': #this gets rid empty quotes right off the bat
            return 0
        if s[0] in '-+':
            if s[1] in '-+': #makes sure there's none of the annoying double -+ stuff
                return 0
            newS = s[0]
            if s[1].isdigit(): #checks if it's a digit or not
                for i in s[1:]:
                    if i.isdigit():
                        newS += i
                    else:
                        break #the moment the iteration is no longer a number
							  #is when we exit out of the for loop
        elif s[0].isdigit():
            newS = ''
            for i in s:
                if i.isdigit():
                    newS += i
                else:
                    break
        else:
            return 0
        if newS == '' or newS == '-' or newS == '+': #again checking to make sure we haven't stripped
													#the code entirely (such as '-abc' which would have
													#exited out of the for loop and resulted as '-')
            return 0
        newS = newS.rstrip('-') 
        newS = newS.rstrip('+')
        newS = int(newS)
        if int(newS) <= -2**31:
            return -2**31
        elif int(newS) >= 2**31 - 1:
            return 2**31 - 1
        return int(newS)
