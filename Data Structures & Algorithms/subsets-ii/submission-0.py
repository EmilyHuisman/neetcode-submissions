class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper( i, nums, subset, curSet):
            if i == len(nums):
                subset.append(curSet.copy())
                return
            curSet.append(nums[i])
            helper(i+1, nums, subset, curSet)
            curSet.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, nums, subset, curSet)
        
        nums.sort()
        subset, curSet = [], []
        helper(0, nums, subset, curSet)
        return subset
            