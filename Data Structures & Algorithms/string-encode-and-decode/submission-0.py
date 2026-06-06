class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            length = str(len(word))
            encoded_string += length + '#' + word
        print(encoded_string)
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        # loop thru and get number, stop at #, convert to int
        # then have an inner loop that for that number loops thru and builds string
        # then appends to list and resets, update counter
        c = 0
        num = ''
        while c < len(s):
            if s[c] == '#':
                word = ''
                i = 1
                while i < (int(num))+1:
                    word += s[c+i]
                    i += 1
                decoded_strs.append(word)
                c += int(num)
                num = ''
            else:
                num += s[c]
            c += 1
        
        return decoded_strs











        for c in range(len(s)):
            num = ''
            while s[c] != "#":
                num += s[c]
                c += 1
            word = ''
            for i in range(int(num)):
                word += s[c+i+1]
            decoded_strs.append(word)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        decoded_string = []
        
        for c in range(len(s)):
            num = ''
            word = ''
            while s[c] != "#":
                num += s[c] # this is a string
                c += 1
            c += 1
            i = c
            while i < int(num):
                word += s[i+c]
            decoded_string.append(word)
            c += int(num)
            num = ''
            word = ''
        return decoded_string