class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        return max(hashMap, key=hashMap.get)