class Solution:


    
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for word in strs:
            encoded_string += str(len(word)) + '#' + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        num = ''
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            decoded_strs.append(s[i:j])

            i = j
        return decoded_strs













































    '''
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            length = str(len(word))
            encoded_string += length + '#' + word
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
        '''
        
        