class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #8/29
        hashset = {}
        for x in nums:
            if x in hashset:
                return True
            hashset[x] = 1
        return False
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        #8/10
        hashSet = {}
        for x in nums:
            if x in hashSet:
                return True
            hashSet[x] = 1
        return False






        
        
        
        
        
        
        
        
        
        
        
        
        
        noDuplicate = set(nums)
        return len(noDuplicate)!= len(nums)
        
        
        
        
        
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap[num] = 1
        return False
'''
        return len(set(nums)) < len(nums)