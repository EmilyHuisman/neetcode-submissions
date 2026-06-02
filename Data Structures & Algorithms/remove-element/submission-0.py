class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[k] = nums[x]
                k += 1
        return k

    

    '''
    loop thry 
    if it doesnt equal it put value thre and then increase k
    '''