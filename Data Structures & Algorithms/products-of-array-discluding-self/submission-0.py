class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i-1]
        print(ans)
        #for i in range(1, nums):
        product = 1
        for j in range(len(nums)-1, 0, -1):
            product *= nums[j]
            ans[j-1] *= product

        return ans