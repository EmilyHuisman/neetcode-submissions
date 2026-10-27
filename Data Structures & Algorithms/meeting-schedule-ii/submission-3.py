"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 10/26
        if len(intervals) < 2:
            return len(intervals)
        start, end = [], []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)

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
                count -= 1
                endPointer += 1
            ans = max(ans, count)
        return ans
                







