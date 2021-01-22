# Leetcode 79. Word Search
# 1/22/21

# Given an m x n board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true




# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false




# Memorize this solution

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return dfs(board, word)
        
        
def visit(board, i, j, word, sindex):
    if len(word) == sindex:
        return True
    
    temp = board[i][j]

    # mark as visited
    board[i][j] = 0
    
    # try visit left
    if j > 0 and board[i][j - 1] == word[sindex]:
        if visit(board, i, j - 1, word, sindex + 1):
            board[i][j] = temp
            return True

    # try visit right
    if j < len(board[0]) - 1 and board[i][j + 1] == word[sindex]:
        if visit(board, i, j + 1, word, sindex + 1):
            board[i][j] = temp
            return True
    
    # try visit up
    if i > 0 and board[i - 1][j] == word[sindex]:
        if visit(board, i - 1, j, word, sindex + 1):
            board[i][j] = temp
            return True
    
    # try visit down
    if i < len(board) - 1 and board[i + 1][j] == word[sindex]:
        if visit(board, i + 1, j, word, sindex + 1):
            board[i][j] = temp
            return True
    
    # we finished with it so unmark it
    board[i][j] = temp
    return False
        
def dfs(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if word[0] == board[i][j]:
                if visit(board, i, j, word, 1):
                    return True
    return False

    
    
    