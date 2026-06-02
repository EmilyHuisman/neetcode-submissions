class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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


        '''

        use a hash map to keep track of the letters and the number of each
        then compare 
        could combine them and then
        '''