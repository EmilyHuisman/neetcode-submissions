class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, nums, target, curSet, combination, setSum):
            if setSum == target:
                #print("targetfound", curSet)
                combination.append(curSet.copy())
                return
            if i + 1 > len(nums):
                return
            if setSum > target:
                setSum = 0
                return
            
            curSet.append(nums[i])
            setSum += nums[i]
            #print("i", i, "sum", setSum, "array", curSet)
            helper(i, nums, target, curSet, combination, setSum)

             
            num = curSet.pop()
            setSum -= num
            helper(i +1, nums, target, curSet, combination, setSum)




        curSet, combination = [], []
        setSum = 0
        helper(0, nums, target, curSet, combination, setSum)
        return combination