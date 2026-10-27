"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 2 arrays (1 start, 1 end)
        # sort them
        # use two pointers approach

        '''
        start: [0, 5, 15]
        end:   [40, 10, 15]


        one pointer at the first end position
        go through 


        '''

        if len(intervals) < 2:
            return len(intervals)
        start, end = [], []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        # use 2 pointers technique
        end.sort()
        start.sort()
        startPointer, endPointer = 0, 0
        count = 0
        ans = 0
        while startPointer < len(start):
            if start[startPointer] < end[endPointer]:
                count += 1
                startPointer += 1
            else:
                ans = max(ans, count)
                count -= 1
                endPointer += 1
        return max(ans, count)
                







