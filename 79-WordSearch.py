# Leetcode 79. Word Search
# Medium 1/15/21 


# Given an m x n board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

 

# Constraints:

#     m == board.length
#     n = board[i].length
#     1 <= m, n <= 200
#     1 <= word.length <= 103
#     board and word consists only of lowercase and uppercase English letters.

# Solution 1 DFS

# Easy Recursive Approach:
# 1. Find the first character in the board and run recursive DFS from that index.
# 2. Recursive DFS to check all the possible directions but stopping if we find the next character to reduce Call Stack Memory and Runtime.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        first_char = word[0]
        
		# Iterating over the board to find the starting character.
        for i in range(len(board)):
            for j in range(len(board[0])):
				# If starting character found and DFS finds the entire word.
                if board[i][j] == first_char and self.dfs(i, j, board, 0, word):
                    return True
        # If we have iterated over the board  completely and did not find the word.
        return False
    
	# Recusive DFS Solution
	# Takes parameters: row, col, board, count (or how many letters we have find yet) and word.
    def dfs(self, row, col, board, count, word):
		# If count == length of "word" (or we have the complete word).
        if count == len(word):
            return True
        
		# Checking for boundaries and also match the present character we are at in "word".
        if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or board[row][col] != word[count]:
            return False
        
		# Instead of using Set or List, we can maintain a temp_char variable to store the character at present index and replace it with the " " space.
		# This will work as "visited" Set or List hence reducing the space complexity.
        temp_char = board[row][col]
        board[row][col] = " "
        
		# Key to avoid TLE is to not make any recursive calls if we find the next character of our word.
		# This is to shorten the state space tree of our algorithm.
		
		# To move down in same column
        if self.dfs(row + 1, col, board, count + 1, word):
			board[row][col] = temp_char
            return True
        
		# To move up in same column
        if self.dfs(row - 1, col, board, count + 1, word):
			board[row][col] = temp_char
            return True
        
		# To move right in same row
        if self.dfs(row, col + 1, board, count + 1, word) :
			board[row][col] = temp_char
            return True
        
		# To move left in same row
        if self.dfs(row, col - 1, board, count + 1, word):
			board[row][col] = temp_char
            return True
			
        # Restoring the temp_char to the board.
        board[row][col] = temp_char
        
		# If none of the above returns True (word not found).
        return False
            








# Solution 2
# Backtracking solution

# This problem is another 2D grid traversal problem which is similar with another problem called 489. Robot Room Cleaner.
# Many people say this is a DFS problem. 
# We can more accurately summarize the solution to be backtracking. 
# Backtracking is a methodology where we mark the current path of exploration, if the path does not lead to a solution, we then rever the change and try another path.

# The skeleton of the algorithm is a loop that iterates through each cell in the grid. For each cell, we invoke the backtracking function to check if we would obtain a solution starating from 
# this very cell.

# For the backtracking function backtrack(row,col,suffix), as a DFS algorithm, it is often implemented as a recursive function.

# The function is broken down to following four steps.
# Step 1 first we check if we reach the bottom case of the recursion, where the word to be matched is empty, we have already found the amtch for each prefix of the word.
# Step 2 Then check if the current state is invalid, either the position of the cell is out of the boundary of the board or the letter in the current cell does not match with the first letter of the word.
# Step 3 If the current step is valid, we then start the exploration of backtracking with the strategy of DFS. First we mark the current cell as visited. Then we iterate through the four possible directions, namely up, right, down, and left.
# Step 4 At the end of the exploration, we revert the cell back to its original state. Finally we return the result of the exploration.

# Solution 1 Backtrack

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret
