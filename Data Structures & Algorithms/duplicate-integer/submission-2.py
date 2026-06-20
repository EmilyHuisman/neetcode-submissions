class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicate = set(nums)
        return len(noDuplicate)!= len(nums)
        
        
        
        
        
        '''hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap[num] = 1
        return False
'''
        return len(set(nums)) < len(nums)