class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        - picking a center letter
        - extending outwards checking if palindrome
            - both letters present / not out of range (*if its equal to letter)
            - same letters
        - once no longer a palindrome, update if max length and store word

        iterate through each letter of the array as cetner

            - expand to both sides
                - check if characters equal and present
                - if not:
                    - check if either side if equal to the cetner and expand untilnot equal
                    - * only after first time

        '''
        ans = ''
        for i in range(len(s)):
            # odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r-l) > len(ans):
                ans = s[l+1:r]
            
            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r-l) > len(ans):
                ans = s[l+1:r]
        
        return ans

            
