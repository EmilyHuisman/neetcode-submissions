class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Given: an int array nums, target value
        Goal: return the indecies of the nums that sum to target

        nums = [4,5,6]
        target = 10

        remiander val = 10 - 4 = 6
        10 - 5 = 5
        10 - 6 = 4
        hashmap: (remainder val, index)
                (4: 0)
                (5: 1)
        when match found = return that index plus current index


        1. loop thru nums array
            a) calculate value needed: k - num
            b) check if value in hashmap
                - if not: add num and index to hashmap
                - if yes:
                    - return vals index and curent index
        '''


        hashmap = {}

        for i, n in enumerate(nums):
            value = target - n
            if value in hashmap:
                return [hashmap[value], i]
            hashmap[n] = i
        




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        
        # 10/07
        remainderDict = {}
        
        for i, x in enumerate(nums):
            remainder = target - x
            if remainder in remainderDict:
                return [remainderDict[remainder], i]
            else:
                remainderDict[remainder] = i
   
        '''


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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