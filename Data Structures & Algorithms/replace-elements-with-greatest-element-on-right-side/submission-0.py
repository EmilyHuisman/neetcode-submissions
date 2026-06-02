class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax

        return arr





















        '''
        arr[len(arr)-2] = arr[len(arr)-1]
        for n in range(2, reversed(arr)):
            if arr[n-1] > arr[n-2]:
                arr[n] = arr[n-1]
            else:
                arr[n] = arr[n-2]
        arr[len(arr)-1] = -1


        '''