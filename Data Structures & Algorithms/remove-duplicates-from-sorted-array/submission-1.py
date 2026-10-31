class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        2 pointers
        one where the next value goes
        one where were chekcing

        if pointers the same; move r pointer
        if pointers diferent, update left pointer and move both
            left pointer + 1 is what we update
        [1,1,2,3,4]

        '''

        l, r = 0, 1

        while r < len(nums):
            if nums[l] == nums[r]:
                r+=1
            else:
                nums[l+1] = nums[r]
                l += 1
                r += 1
        return l+1