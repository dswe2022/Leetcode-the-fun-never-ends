# Leetcode 253. Meeting Rooms II 
# Medium 12/29/20 
# https://medium.com/@edward.zhou/leetcode-253-meeting-rooms-ii-explained-python3-solution-3f8869612df

# Problem Description

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
# (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

# Solution

# This solution actually mimic what a human being will do. Imaging when you have a series of meetings to start, 
# first you will sort them (with O(N logN) and then when you 
# look at first meeting starting time, you will wonder if there is a meeting ends 
# (that means a meeting room is released), if yes, you will just take that one; otherwise, you will find a new room.

# There are one tip here: how to find a meeting room quickly that’s available when a meeting 
# (for example, A) starts? Below I will sort ending times and check the first one(let’s name it B), 
# if A.startTime ≥ B.endTime, then actually A can re-use the same meeting room A uses and in the same time, 
# the end time is removed since it’s already evaluated (as a possible precedent of another meeting); if not, 
# since B is the first one (and the earliest one) that ends, then I don’t need to check others end times and 
# will just add room number by 1 since a new room will be needed.

# The way that breaks starting and ending times apart could be confusing.Please follow below example to get 
# better understanding:

#     assume I have this as intervals: [(1,3),(9,18),(3,7),(6,12),(4,9)]
#     startTimes will be [1,3,4,6,9] and endTimes will be [3,7,9,12,18])
#     to start, pick the first start time which is 1, let’s see if I can put it after some meeting (logically speaking,
#     I cannot since that’s the earliest meeting), at this moment, the smallest end time is 3, so certainly I cannot find 
#     an existing available room. So rooms will be added by 1 to be 1 (since its original value is 0).
#     now move to the second start time which is 3, notice that the earliest end time is 3, which means a meeting will end 
#     at 3 and its room will be released, I don’t need to ask for another new room. So I will move to arrange next meeting 
#     while in the same time remove the used end time 3.
#     now the startTimes will be [4,6,9] and endTimes will be [7,9,12,18]. 4 < 7, so rooms +=1 to become 2. Next 6 < 7, so 
#     again rooms +=1 to become 3. Then 9 > 7, so this meeting can reuse a pre-occupied meeting room, now startTimes will be 
#     [] and endTimes will be [9,12,18].
#     OK, although endTimes is not yet cleared, startTimes is empty meaning I have arranged all meetings. That’s it. 
#     Return rooms which is 3 and it’s the desired answer!




class Solution(object):
    def minMeetingRooms(self, intervals):
        startTimes = [i[0] for i in intervals]
        endTimes = [i[1] for i in intervals]
        startTimes = sorted(startTimes)
        endTimes = sorted(endTimes)
        rooms = 0
        while(len(startTimes) > 0):
            startTime = startTimes.pop(0)
            #now a meeting is going to start, is there a meeting ends
            #(meaning a meeting room is released)?
            endTime = endTimes[0]
            if endTime <= startTime:
                endTimes.pop(0)
            else:
                #need to ask for a new room
                rooms += 1
        return rooms

# T: O(a)
# S: O(a)