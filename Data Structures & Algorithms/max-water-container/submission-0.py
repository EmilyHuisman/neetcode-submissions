class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start from ends
        # calculate vol
        # move the pointer with the pointer with the lest value forward
        # reculate vol and if larger store

        l, r = 0, len(heights)-1
        maxVol = 0
        while l < r:
            vol = (r-l) * min(heights[l], heights[r])
            maxVol = max(maxVol, vol)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1
        return maxVol