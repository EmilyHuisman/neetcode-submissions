class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        '''
        reverse the right half of the number

        do this until 




        1 2 1

        ------
        1 2
        1
        ------
        1
        1 2



        '''
        if x == 0:
            return True
        if x%10 == 0:
            return False
        
        rev = 0
        while rev < x:
            rev = rev * 10 + (x % 10)
            x = x // 10

        
        if rev == x or (rev // 10) == x:
            return True
        

        return False





