class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pass
        '''
        k = 5
        [2,5,1,3]
        sum = 11
        target = 6
        


        1. target sum = sum of array - x, also running sum
        2. implement "sliding windows" technique: 2 pointers, L, R
        Loop thru until right is at the end of array
            a) add R pointer to sum
            b) check if sum = target
                - if yes: we will update ans to max length
                - if no: 
                    - if its greater than:
                        - subtract left pointer from sum
                        - just move left 
                    - if its less:
                        - move right
        3. return len(array) - ans

        '''

        # [4, 2, 4]
        # target = 7
        #
        target = sum(nums) - x
        total = 0
        l = r = 0
        maxLength = 0

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        while r < len(nums):
            total += nums[r]
            
            while total > target:
                total -= nums[l]
                l += 1
            if total == target:
                maxLength = max(maxLength, r - l + 1)
            r += 1
        if maxLength == 0:
            return -1
        return len(nums) - maxLength
            


















