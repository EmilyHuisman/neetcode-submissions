class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        pass

        '''
        Goal: return the greatest score

        Rules it has to follow:
            - if we add a value, values one smaller or larger cannto be added

        [1,1,2,3]
        [1,2,3]


        *hashmap that has freuqencies
        first count the occurances of each value
        make it a set


        1. make hashmap of value frequencies
        2. remove duplicates & sort
        3. loop thru array
            - prev, curr
            - check if you can include curr (so not within 1)
            - if not include prev
        '''


        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, 0
        
        for i in range(len(nums)):
            total = nums[i] * count[nums[i]]
            if nums[i] == nums[i-1] + 1:
                temp = earn2
                earn2 = max(total+earn1, earn2)
                earn1 = temp
            else:
                earn1 = earn2
                earn2 += total
        
        return earn2
                
            









