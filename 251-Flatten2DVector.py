# Leetcode 251. Flatten 2D Vector
# Medium 12/29/20 


# Implement an iterator to flatten a 2d vector.

# For example,

# Given 2d vector =

# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]

# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.



class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.row, self.col = 0, 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext() is False: return None
        self.col += 1
        return self.vec2d[self.row][self.col-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec2d) and self.col == len(self.vec2d[self.row]):
            self.col, self.row = 0, self.row + 1

        return self.row != len(self.vec2d)