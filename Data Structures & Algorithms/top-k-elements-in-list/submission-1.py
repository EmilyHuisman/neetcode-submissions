class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #08/30
        count = defaultdict(int)

        for x in nums:
            count[x] += 1
        
        bucketSort = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucketSort[freq].append(num)
        

        ans = []
        for freq in range(len(bucketSort)-1, 0, -1):
            for num in bucketSort[freq]:
                if k > 0:
                    ans.append(num)
                    k -= 1
        
        return ans
































        '''
        # 06/08/26
        hashMap = defaultdict(int)
        
        for num in nums:
            hashMap[num] += 1
        
        bucketSort = [[] for _ in range(len(nums)+1)]

        for num, freq in hashMap.items():
            bucketSort[freq].append(num)
        
        ans = []
        for freq in range(len(bucketSort)-1, 0, -1) :
            for num in bucketSort[freq]:
                if k > 0:
                    ans.append(num)
                    k -= 1

        return ans
        
        
    
      
        # hashmap where the keys are the freq count, value is the #
        # traverse hashmap until k is met
        # use bucket sort

        count = defaultdict(int)
        bucketSort = [[] for _ in range(len(nums)+1)]
        ans = []
        for num in nums:
            count[num] += 1 # num - count
        
        for num, freq in count.items():
            bucketSort[freq].append(num)

        for i in range(len(bucketSort)-1, 0, -1): # goes thru it in reverse
            for num in bucketSort[i]:
                if k > 0:
                    ans.append(num)
                    k -= 1
        return ans
        '''

        
        
        
        
        
        
        
        
        
        
        
        '''
        # make dict w/ frequencies key - value: number - freq
        # then use bucketsort where indices = freq
        # take the first k
        bucketSort = [[] for _ in range(len(nums)+1)]
        freq = defaultdict(int)
        ans = []
        for num in nums:
            freq[num] += 1
        
        for num, count in freq.items():
            bucketSort[count].append(num)

        for i in range(len(bucketSort) -1, 0, -1):
            for num in bucketSort[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        '''