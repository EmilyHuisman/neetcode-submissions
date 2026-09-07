class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #09/07


        ans = 0
        l, r = 0, len(heights)-1

        while l < r:
            vol = (r-l) * min(heights[l], heights[r])

            ans = max(ans, vol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
        return ans 



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        # 06/11
        # start from ends
        # calculate vol
        # move the pointer with smaller value forward - only way to potentially increase vol
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
        '''