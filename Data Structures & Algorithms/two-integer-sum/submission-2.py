class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #08/29
        target_dict = {}
        comp = 0
        for x in range(len(nums)):
            comp = target - nums[x]
            if comp in target_dict:
                return [target_dict[comp], x]
            target_dict[nums[x]] = x
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        #8/06
        hashMap = {}
        temp = 0

        for x in range(len(nums)):
            temp = target - nums[x]
            if temp in hashMap:
                return [hashMap[temp], x]
            hashMap[nums[x]] = x















        
        hashMap = {}
        res = 0
        for x in range(len(nums)):
            res = target - nums[x]
            if res in hashMap:
                return [hashMap[res], x]
            hashMap[nums[x]] = x
        

        
        key - value pair
        key is the num, value is the num needed to make target
        maybe key is the value needed to make target, value is the index

        iterate thru list and check is res is in hash map, if not add

        '''