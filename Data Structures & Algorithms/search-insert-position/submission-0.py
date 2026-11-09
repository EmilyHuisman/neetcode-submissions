class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        do a bs
        move low high mid pointers
        f found return
        elsedo l+1

        '''
        low, high = 0, len(nums)

        while low < high:
            mid = (low+high)//2
            if target < nums[mid]:
                high = mid
            elif target > nums[mid]:
                low = mid+1
            else:
                if target == nums[mid]:
                    return mid
            
        return low