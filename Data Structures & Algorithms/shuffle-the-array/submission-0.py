class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        

        '''
        2 pointers tech

        intialize both pointers
        1 at the start
        1 at the midway point (=n)

        iterate thru both pointers
        adding numbers to ans array

        '''


        first, second = 0, n
        ans = []
        while first < n:
            ans.append(nums[first])
            ans.append(nums[second])
            first += 1
            second += 1
        
        return ans

















