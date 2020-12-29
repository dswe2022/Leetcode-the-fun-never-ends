# Leetcode 62. Unique Paths
# Medium 12/28/20


# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach 
# the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?


# Use dynamic programming to solve.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dmap = [[0] * n for _ in range(m)]
        for i in range(m):
            dmap[i][0] = 1
        for j in range(n):
            dmap[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                l = u = 0
                if i-1 >= 0:
                    u = dmap[i-1][j]
                if j-1>= 0:
                    l = dmap[i][j-1]
                dmap[i][j] = l + u
        return dmap[m-1][n-1]

# T: O(m*n)
# S: O(m*n)