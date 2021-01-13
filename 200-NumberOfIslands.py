# Leetcode 200 Number of Islands
# Medium 12/17/20 

# Given an a by b 2d grid map of "1" s (land) and "0" (water), return the number of islands.



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