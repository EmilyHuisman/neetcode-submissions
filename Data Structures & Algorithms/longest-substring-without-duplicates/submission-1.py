class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #09/10
        hashset = set()
        L = 0
        ans = 0

        for R in range(len(s)):
            while s[R] in hashset:
                hashset.remove(s[L])
                L+=1
            hashset.add(s[R])
            ans = max(ans, R-L+1)

        return ans