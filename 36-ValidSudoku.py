# Leetcode 36. Valid Sudoku
# Medium 12/29/20 

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to
# the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.

 

 class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                if c + '@row ' + str(i) in seen or c + '@col ' + str(j) in seen or c + '@box ' + str(i // 3) + str(j // 3) in seen:
                    return False
                seen.add(c + '@row ' + str(i))
                seen.add(c + '@col ' + str(j))
                seen.add(c + '@box ' + str(i // 3) + str(j // 3))

        return True

# T: O(1), the for loop iterations don't expand.
# S: O(1), the board doesn't expand.

