class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        Goal: return length longest subarray that contains same amount of 1 and 0, otherwise 0


        [-1,1,1,-1,1,-1] 
        k = 0

        hashmap {values, store the first occurance index}
        {0:0, -1: 1, 1: 3}

        * whenever we find an answer take the max of that ans answer


        1. initalize int ans, int sum, int dif, hashmap prefix sum
        2. loop thru array
            a) if its 0 change to -1
            b) calculate sum
            c) find diff by multiply by -1
            d) check hashmap for value
            e) if its present update ans to max length
            f) add index to hashmap if not already present
        3. return ans

        '''

        # [0,0,1]
        curSum = diff = ans = 0
        prefixSum = {0: 0}

        for i, num in enumerate(nums):
            if num == 0:
                num = -1
            curSum += num
            diff = curSum

            if diff in prefixSum:
                ans = max(ans, i + 1 - prefixSum[diff])
            
            if curSum not in prefixSum:
                prefixSum[curSum] = i+1
        
        return ans












