# Leetcode 200 Number of Islands
# Medium 12/17/20 

# Given an a by b 2d grid map of "1" s (land) and "0" (water), return the number of islands.

# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.



class Solution(object);
    def numIslands(self, grid):
        counter = 0
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                if grid[row][col] == "1":
                    counter +=1
                    self.dfs(row,col,grid)
        return counter

    #Flip the land into water part.
    def dfs(self,row,col,grid):
        if row >= 0 and row<len(grid) and col>=0 and col<len(grid[0] and grid[row][col] == "1":
            grid[row][col] = "0"
            self.dfs(row-1, col,grid)
            self.dfs(row+1,col,grid)
            self.dfs(row,col-1,grid)
            self.dfs(row,col+1,grid)
            




# Time: O(a*b), a is the length of row and b is the length of the col.
# Space: O(1), constant time.




# Solution 1 DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        q = collections.deque()
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0" or
                (r, c) in visit):
                return
            
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands





# Solution 2 BFS


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        q, visit = collections.deque(), set()    
        islands = 0
        
        def bfs(r, c):
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ( r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c) not in visit 
                       ):
                        q.append((r, c))
                        visit.add((r, c))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands