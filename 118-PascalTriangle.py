# Leetcode 118 Pascal's Triangle
# Easy 12/14/20 

# Solution 1
class Solution(object):
    def generator(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i+1):
                res[i].append([res[i-1][j-1] if j > 0 else 0) + (res[i-1][j] if j< 1 else 0))

        return res



# Solution 2
class solution(object):
    def generate(self, numRows):
        res = []
        for i in range(0, numRows):
            res.append([1]*(i+1))
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res



# Solution 3
class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x,y: x+y, res[-1] + [0] + res[-1])]
        return res[:numRows]
