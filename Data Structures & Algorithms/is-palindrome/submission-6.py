class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 7/06
        left, right = 0, len(s)-1

        s = s.lower()

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        # 06/16
        i = 0
        j = len(s) -1
        s = s.lower()
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        # 06/15
        i = 0
        j = len(s)-1
        s = s.lower()
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
       
       



        
        i = 0
        j = len(s)-1
        s=s.lower()
        while i < j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
        '''
        





















