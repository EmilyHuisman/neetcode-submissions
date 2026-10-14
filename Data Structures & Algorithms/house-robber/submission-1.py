class Solution:
    def rob(self, nums: List[int]) -> int:
        # subproblems are the parings
        # every index is the sum of teh prevous index -1 plus itself
        # return max once the end is reached
        # return max of odd vs even
        if len(nums) == 1:
            return nums[0]

        '''i = 2
        while i < len(nums):
            if i % 2 == 0:
                dp[0] += nums[i]
            else:
                dp[1] += nums[i]
            i+=1
        
        return max(dp)
'''
        # plus all the sums that its not touching and then its the max of those
        # add, dont add

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # we have to switch
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]