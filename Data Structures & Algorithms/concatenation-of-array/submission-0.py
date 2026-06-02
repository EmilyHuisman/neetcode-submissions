class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        capacity = 2 * n 
        ans = [0] * capacity
        ans = nums + nums
        return ans