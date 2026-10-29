class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [1, 2, 3, 4]
        h = 9
        k = ?

        start at middle point

        - everything to the Left of 3 can be eaten within an hour
        - to the R we would calculate how much time
        - compare if time is G/L than h
        - if its greater move R
        - if its less that move L

        the middle should always be the average of the two sides


        min = 1
        max = max(piles)

        take middle 

        everything below middle is within an huor
        everythign above do // with ciel upervound and add
        if its below move L, if its less move R


        1. calculate middle
        2. find pivot in piles where its less than, iterate thru more than values doing ciel by k value


        '''


        low = 1
        high = max(piles)
        hours = 0
        while low < high:
            mid = (low + high) // 2
            hours = sum((p+mid-1)//mid for p in piles)
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return high


















