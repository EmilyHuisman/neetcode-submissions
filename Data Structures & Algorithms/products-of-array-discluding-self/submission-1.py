class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        # [1, 1, 2, 8]
        # [1, 2, 4, 6]
        print(output)
        mult = 1
        for x in range(len(nums)-1, 0, -1):
            mult *= nums[x]
            output[x-1] *= mult
        return output


        '''
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
        '''