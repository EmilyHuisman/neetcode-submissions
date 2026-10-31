class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        low = 0
        mid = 0
        high = len(nums)

        iterate thru array
            - if nums[mid] == 0:
                - swap the number at low with value
                - advance both low and mid pointers
            - if mid == 2:
                - swap mid with high
                - decrease high
            - if mid = 1:
                - advance mid

        '''


        low = mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        


