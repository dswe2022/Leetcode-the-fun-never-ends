# Leetcode 240. Search a 2N Matrix II
# Medium 12/31/20

# Write an efficient algorithm that searches for a target value 
# in an m x n integer matrix. The matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Solution

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        else:
            no_rows = len(matrix)
            no_cols = len(matrix[0])

            if target < matrix[0][0] or target > matrix[no_rows-1][no_cols-1]:
                return False
            else:
                r = 0
                c = no_cols-1

                while r < no_rows and c >=0:
                    if matrix[r][c] == target:
                        return True
                    elif target > matrix[r][c]:
                        r += 1
                    elif target < matrix[r][c]:
                        c -= 1
                return False

# T: O(a)
# S: O(1)