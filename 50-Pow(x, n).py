# Leetcode 50. Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

 

# Constraints:

#     -100.0 < x < 100.0
#     -231 <= n <= 231-1
#     -104 <= xn <= 104




class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        
        postive = n > 0
        n = abs(n)

        count = 0
        res = 1

        step = 1
        tmp = x
        
        while count < n:
            if count + step > n:
                step = 1
                tmp = x
                
            res = res * tmp
            count += step
            
            step = step * 2
            tmp = tmp * tmp
            
        return res if postive else 1/res
        
# T: O(a)
# S: O(1)



# Solution 2
# O(logN) Non Recursive
class Solution2(object):
   def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = - n
        
        product = x
        ans = 1
        index = n
        while(index > 0):
            if index % 2 == 1:
                ans = ans * product

            product = product * product
            index //= 2

        return ans

# T: O(log(a))
# S: O(1)


# Solution 3
# O(logN) Recursive
class Solution3(object):
    def recursivePow(self, x, n):
        if n == 0:
            return 1.0

        half = self.recursivePow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = - n
        
        return self.recursivePow(x, n)

# T: O(log(a))
# S: O(1)