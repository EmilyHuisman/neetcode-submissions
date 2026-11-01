class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''

        Given: array nums
        Goal: return largest product from subarray



        [-2,4,0,-3,5]

        min = min(curMin * x, x, curMax*x)
        max = max(curMin * x, x, curMax*x)

        

        '''


        curMin = nums[0]
        curMax = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            tempMin = curMin
            curMin = min(curMin * num, num, curMax * num)
            curMax = max(tempMin * num, num, curMax * num)
            ans = max(curMin, curMax, ans)
        return ans
            