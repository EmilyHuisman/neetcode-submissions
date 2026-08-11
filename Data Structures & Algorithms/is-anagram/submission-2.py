class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #8/12
        hashMap = {}
        if len(s) != len(t):
            return False

        for c in s:
            if c not in hashMap:
                hashMap[c] = 1
            else:
                hashMap[c] +=1
        for c in t:
            if c not in hashMap:
                return False
            hashMap[c] -=1
            if hashMap[c] == 0:
                del hashMap[c]
        
        return len(hashMap) == 0








        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        if len(s) != len(t):
            return False
        hashMap = {}
        for x in s:
            if x not in hashMap:
                hashMap[x] = 1
            else:
                hashMap[x] += 1
        
        for j in t:
            if j not in hashMap:
                return False
            hashMap[j] -= 1
            if hashMap[j] == 0:
                del hashMap[j]

        return len(hashMap) == 0           




        use a hash map to keep track of the letters and the number of each
        then compare 
        could combine them and then
        '''