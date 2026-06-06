class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we know anythign before 


        # out everything in a set to avoid duplicates
        # hash map to store length alrdy
        numSet = set(nums)
        longest = 0
  
        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                i = 1
                while num + i in numSet:
                    count += 1
                    i += 1
                if count > longest:
                    longest = count
        return longest