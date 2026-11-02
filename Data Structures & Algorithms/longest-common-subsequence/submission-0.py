class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Given: 2 words
        Goal: return the len of longest common subsequence


        text1 = "cazt"

        text2 = "crabt" 

        when both letters equal -> we advance in both words
        when not equal -> we advance in either, 2 options

            c   a   b   t  -> text 1 
        c    
        
        r

        a

        b           2   1

        t           1   1
            0   0   0   0
        
        prevrow = [0] * len(text1) +1

        1. loop thru each row
            a) iniitalize curr row = [0] * len(text1)
            b) loop thru each coloum:
                - text1[col] == text2[row]:
                    currow[col] = prevcol[c+1] +1
                else:
                    currow[col] = max(prevrow[c], currow[c+1])
            c) prevrow = currow


        '''


        row, col = len(text1), len(text2)
        prevRow = [0] * (col + 1)

        for r in range(row-1, -1, -1):
            currRow = [0] * (col + 1)
            for c in range(col-1, -1, -1):
                if text1[r] == text2[c]:
                    currRow[c] = prevRow[c+1] + 1
                else:
                    currRow[c] = max(currRow[c+1], prevRow[c])
            prevRow = currRow
        
        return currRow[0]







