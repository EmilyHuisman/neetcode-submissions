class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''

        Given: list of intervals
        Goal: return set of non overapping intervals


        * sort the intervals array
        
        Conditions:
            - interval overlaps if its start value if less than the previous end value

        1. sort the intervals array
        * start, end pointer
        2. loop thru the intervals
            - compare the start time with end pointer:
                - if its less than or equal:
                    - update the end pointer to be the max of the two values
                - if its greater:
                    - add previous end start pointer vals to ans
                    - update both pointers to new times
            add end start pointer values
        3. return ans


        '''

        intervals = sorted(intervals)

        startPointer, endPointer = intervals[0][0], intervals[0][1]
        ans = []

        for start, end in intervals:
            if start <= endPointer:
                endPointer = max(endPointer, end)
            else:
                ans.append([startPointer, endPointer])
                startPointer = start
                endPointer = end
        ans.append([startPointer, endPointer])
        return ans

        












