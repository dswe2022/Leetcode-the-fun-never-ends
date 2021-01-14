# Leetcode 295. Find Median from Data Stream
# Hard 1/14/21

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# For example,

# [2,3,4], the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

#     void addNum(int num) - Add a integer number from the data stream to the data structure.
#     double findMedian() - Return the median of all elements so far.

 

# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

 

# Follow up:

#     If all integer numbers from the stream are between 0 and 100, how would you optimize it?
#     If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?





class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def addNum(self, num: int) -> None:
        # add the number than sort it.
        self.arr.append(num)
        self.arr.sort()
        
    def findMedian(self) -> float:
        mid = len(self.arr)//2
        if len(self.arr) == 0:
            return 0
        if len(self.arr) == 1:
            return self.arr[0]
        
        
        if len(self.arr) % 2 == 0:
            #even
            return (self.arr[mid] + self.arr[mid-1]) / 2
        else:
            #odd
            return self.arr[mid]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# Solution 2 Very fast


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = []
        self.larger = []
        

    def addNum(self, num: int) -> None:
        if len(self.smaller) == len(self.larger):
            heapq.heappush(self.larger, -heappushpop(self.smaller, -num))
        else:
            heapq.heappush(self.smaller, -heappushpop(self.larger, num))
        

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.larger):
            return float(self.larger[0] - self.smaller[0]) / 2
        return self.larger[0]



# Solution 3
# Python3 min heap + max heap faster than 99%


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_ = []
        self.min_ = []

    def addNum(self, num: int) -> None:
        if self.max_:
			# always remember to invert when push to/pop from a max heap
            if num >= -self.max_[0]:
                heapq.heappush(self.min_, num)
            else:
                heapq.heappush(self.max_, -num)
        else:
            if not self.min_:
                heapq.heappush(self.max_, -num)
            else:
                if num <= self.min_[0]:
                    heapq.heappush(self.max_, -num)
                else:
                    heapq.heappush(self.min_, num)
        
        while abs(len(self.min_) - len(self.max_)) > 1:
            if len(self.min_) > len(self.max_):
                extract = heapq.heappop(self.min_)
                heapq.heappush(self.max_, -extract)
            else:
                extract = -heapq.heappop(self.max_)
                heapq.heappush(self.min_, extract)

    def findMedian(self) -> float:
        if len(self.min_) == len(self.max_):
            a, b = self.min_[0], -self.max_[0]
            return (a + b) / 2
        if len(self.min_) > len(self.max_):
            return self.min_[0]
        
        return -self.max_[0]
