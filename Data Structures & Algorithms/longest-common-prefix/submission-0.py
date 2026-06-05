class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for c in range(len(strs[0])): # the characters
            for i in strs: # the words
                if c == len(i) or i[c] != strs[0][c]:
                    return i[:c]
        return strs[0]