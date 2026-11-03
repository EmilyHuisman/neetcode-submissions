class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Given: m by n grid
        Goal: return # of possible unique paths form start to finish
        Constrants:
            - move to the right
            - move down

        
            0   1   2   3
        0.  6   3   1   0

        1.  3   2   1   0

        2   1   1   G   0

        3  0    0   0   0   


        1. initalize a prev row array len cols
        2. loop thru the rows in reverse
            a) curr row = [0] * len(cols)
            b) loop thru the columns
                c) we will update the value to be the sum of bottom and right
            prev = cur row
        3. return value at currow[0]


        '''

        prevRow = [0] * n

        for r in range(m-1, -1, -1):
            curRow = [0] * n
            curRow[n-1] = 1
            for c in range(n-2, -1, -1):
                curRow[c] = prevRow[c] + curRow[c+1]
            prevRow = curRow
        return curRow[0]











