class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
        