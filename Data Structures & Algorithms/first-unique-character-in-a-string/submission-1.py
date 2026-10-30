class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        
        return -1
        '''

        dictionary : {(index, character): values }

        iterate thru characters in s:
            - check if its in dict
                - if yes: update count value
            - if no: add it to dict with its index
        
        search dict values for 1
            - return first occurnace, index
        - return -1


        have the dict be
        "char" -> [index, count]
        

        charDict = {}

        for i, c in enumerate(s):
            if c in charDict:
                charDict[c][1] += 1
            else:
                charDict[c] = [i, 1]


        for c, (i, count) in charDict.items():
            if count == 1:
                return i


        return -1 
        '''

