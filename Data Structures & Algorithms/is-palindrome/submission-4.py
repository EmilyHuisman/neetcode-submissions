class Solution:
    def isPalindrome(self, s: str) -> bool:
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
        





















