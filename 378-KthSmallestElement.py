# Leetcode 378. Kth Smallest Element in a Sorted Matrix
# Medium 12/28/20

# Given a n x n matrix where each of the rows and columns are sorted in ascending order,
# find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.



import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        temp = [[False] * n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        temp[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not temp[i + 1][j]:
                temp[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not temp[i][j + 1]:
                temp[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans


# T: O(a)
# S: O(a), using a heap.


# Runner code

matrix = [
   [0, 5, 9],
   [11, 12, 13],
   [15, 17, 19]   
]
k = 1
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("First smallest element:",result)
k = 2
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("\nSecond smallest element:",result)
k = 3
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("\nThird smallest element:",result)

