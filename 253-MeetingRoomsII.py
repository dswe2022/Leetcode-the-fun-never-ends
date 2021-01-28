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



# Solution 1
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

# Solution 2 Priority queue 
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

# T: O(alog(a))
# S: O(a)


# Solution 3 Chronological ordering

# Separate out the start times and the end times in their separate arrays.
# Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.
# We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
# When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. If this is the case then that would mean some meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
# If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.
# Repeat this process until s_ptr processes all of the meetings.
# Let us not look at the implementation for this algorithm.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms

# T: O(alog(a))
# S: O(a)