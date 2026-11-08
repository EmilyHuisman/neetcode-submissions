class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        start at the end
        check to see if word is in bnank, check length first
        if yes then change that position to true, else dont
        '''

        valid = [False] * (len(s) +1)
        valid[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if len(s[i:]) >= len(word) and s[i:i+len(word)] == word and valid[i+len(word)] == True:
                    print(s[i:i+len(word)], word)
                    valid[i] = True
                if valid[i]:
                    break
                print(valid[i])
        return valid[0]