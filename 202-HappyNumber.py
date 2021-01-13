# Leetcode 202 Happy Number
# Easy 12/18/20

# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# hose numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Solution 1
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        temp = []
        while True:
            for i in str(n):
                sum += int(i)**2
            n = sum
            if n in temp:
                break
            else:
                temp.append(n)
            sum = 0
            
        if n == 1:
            return True
        else:
            return False

# Time: O(n)
# Space: O(n)


# Solution 2

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_dict = {}
        while True:
            num_dict[n] = True
            sum = 0
            while n>0:
                sum += (n%10) *(n%10)
                n/=10
            if sum == 1:
                return True
            elif sum in num_dict:
                return False
            else:
                n = sum


# Time: O(n^2)
# Space: O(n)


# Solution 3

def isHappy(n):
    happySet = set([1,7,10,13,19,23,28,31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97])
    while n> 99:
        n = sum([int(x)* int(x) for x in list(str(n))])
    return n in happySet

# Time: O(n)
# Space: O(n)



# Solution 4
# Floyd Cycle Detection Algorithm

class Solution(object):
    def isHappy(self,n):
        slow = fast = n
        while True:
            slow = self.squareSum(slow)
            fast = self.squareSum(fast)
            fast = self.squareSum(fast)
            if slow == fast:
                break
        return slow == 1

    def squareSum(self,n):
        sum = 0
        while n>0:
            temp = n %10
            sum += temp *temp
            n/=10
        return sum

# Time: O(n)
# Space: O(n)

