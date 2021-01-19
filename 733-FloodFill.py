
# Leetcode 733. Flood Fill
# Easy 1/18/21

# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

# Example 1:

# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

# Solution 1


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # Calcuate the length of rows and columns.
        R = len(image)
        C = len(image[0])
        
        # check the color and set the current color from the origin coord.
        color = image[sr][sc]
        # if color of origin coord is newColor, just return image.
        if color == newColor:
            return image
        
        # No return function. Just flip the numbers.
        # Put the dfs function inside floodFill function so you don't 
        # have to keep copying the image board. Because the same image board
        # is in same scope, you don't have to keep passing it into dfs().
        # Also, you don't have to keep passing in the row and col bounds.
        def dfs(row,col):
            if image[row][col] == color:
                image[row][col] = newColor
                if row >= 1:
                    dfs(row-1, col)
                if row +1 < R:
                    dfs(row +1, col)
                if col >= 1:
                    dfs(row, col-1)
                if col+1 < C:
                    dfs(row, col +1)
        
        dfs(sr,sc)
        return image
        
        