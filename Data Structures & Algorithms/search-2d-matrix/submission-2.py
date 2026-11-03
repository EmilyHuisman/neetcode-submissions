class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Given: m x n matric in nondecreasng order
        Return: true of target val found


        1. Find correct row
        2. 2 pointers approach that starts at low and high pointer
            a) if val > high -> mve down a row
            b) perform binary search on row ->return True if we find value



        
        L       H      
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
        
        target: 13

        mid = (L+H) // 2
        '''
        lastCol = len(matrix[0])-1
        for row in range(len(matrix)):
            low, high = matrix[row][0], matrix[row][lastCol]
            if target <= high:
                l, r = 0, lastCol
                while l <= r:
                    mid = (l + r + 1) // 2 # double slashes rounds down
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            
        return False


                
            