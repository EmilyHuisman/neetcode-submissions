class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        * sliding window technique

        2 points (L, R) on s2
        - move R pointer if letter is in s1 and remove letter from s1
        - if not move L pointer and addletter that it moves from back to s1

        '''

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in s1:
            s1Count[ord(i)-ord('a')] += 1
        
        l = r = 0

        while r < len(s2):
            if (r - l + 1) > len(s1):
                s2Count[ord(s2[l])-ord('a')] -= 1
                l += 1
            
            s2Count[ord(s2[r])-ord('a')] += 1
            r += 1
            if s1Count == s2Count:
                return True
        return False