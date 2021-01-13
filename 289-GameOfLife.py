# Leetcode 289 Game of Life
# Medium 12/27/20 


# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

#     Any live cell with fewer than two live neighbors dies, as if caused by under-population.
#     Any live cell with two or three live neighbors lives on to the next generation.
#     Any live cell with more than three live neighbors dies, as if by over-population.
#     Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

 # Solution 1

 class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = 0
                
                for x, y in direction:
                    if 0 <= i + x < len(board) and 0 <= j + y < len(board[i]):
                        count += (board[i + x][j + y] & 1)
                
                # condition 2
                if (board[i][j] & 1) == 1 and (count == 2 or count == 3):
                    board[i][j] = 0b11
                    
                # condition 4
                if (board[i][j] & 1) == 0 and count == 3:
                    board[i][j] = 0b10
                    
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] >>= 1


# T: O(a)
# S: O(a)