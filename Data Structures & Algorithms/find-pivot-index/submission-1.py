class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # create prefix sum array
        # loop thru indicies and check if left = right
        '''
        arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            arr[i + 1] = arr[i] + nums[i]
        
        for j in range(len(nums)):
            left = arr[j]
            right = arr[len(nums)] - arr[j+1]
            if left == right:
                return j
        return -1

        '''


        total = 0
        for num in nums:
            total += num
        
        leftSum = 0

        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1