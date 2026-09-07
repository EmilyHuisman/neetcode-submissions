class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array

        # loop through the array, kip any uplicate pairs --> ensure that we dont return any duplicate triplets

        # left and right pointer
        # if the sum is positive well move the right pointer, if its negative well ove the left pointer --/ ski fduplicates -- > left , right


        #i, left, right = 0, i + 1, len(nums)-1
        
        nums.sort()
        ans = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1

            while l < r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1
        return ans


            






        '''
            while nums[i] == nums[i+1] and i < len(nums)-2: 
                i += 1
            left = i + 1
            right = len(nums)-1

            sum = nums[i] + nums[left] + nums[right]

            while sum > 0 and left<right:
                right -= 1
            
            while sum < 0 and left<right:
                left += 1
            
            if sum == 0:
                ans.append[nums[i], nums[left], nums[right]]       
        return ans 
        
  
        nums.sort()
        ans = []

        for i, a in enumerate(nums):
            if a >0:
                break
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ans
        '''