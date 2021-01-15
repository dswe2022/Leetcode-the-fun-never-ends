# Leetcode 212. Word Search II
# Medium 1/15/21 

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:

# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

 

# Constraints:

#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 12
#     board[i][j] is a lowercase English letter.
#     1 <= words.length <= 3 * 104
#     1 <= words[i].length <= 10
#     words[i] consists of lowercase English letters.
#     All the strings of words are unique.

# Solution 1 dfs 


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result=set()
        def dfs(i,j,c,word):
            if i<0 or j <0 or i>=len(board) or j >= len(board[0]) or board[i][j]!=word[c]:
                return False
            if c==len(word)-1:
                return True
            c+=1
            b=board[i][j]
            board[i][j]='t'
            found= dfs(i,j+1,c,word) or dfs(i,j-1,c,word) or dfs(i+1,j,c,word) or dfs(i-1,j,c,word)
            board[i][j]=b
            return found
        for w in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==w[0]:
                        if dfs(i,j,0,w):
                            result.add(w)

        return result




# T: O(w,i,j), where w is length of word, i is number of rows, and j is number of cols.
# S: O(a), set.