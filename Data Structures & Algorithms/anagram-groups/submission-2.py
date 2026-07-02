class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #7/2
        hashMap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            hashMap[tuple(count)].append(word)
        return list(hashMap.values())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        












        '''
        hashMap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord('a')] += 1
            hashMap[tuple(count)].append(word)
        
        return list(hashMap.values())
        '''



























        '''
        # hashmap where key holds the letter count for each word
        # loop thru each word and add to hashmap
        # traverse thru and append
        # make sure to make the array a tuple since keys must be immutable





        hashMap = defaultdict(list)


        for word in strs:
            count = [0] * 26
            for c in word:
                count[(ord(c)- ord('a'))] += 1
            hashMap[tuple(count)].append(word)

        return list(hashMap.values())
        '''























        '''
        # have a hashmap that will stores: word, index
        # loop through the list and create sorted word
        # agasinst hash map check if sroted word exists, if no add to hash map
        # if yes add to list


        ans = []
        hashMap = {}
        i = 0
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in hashMap:
                hashMap[sortedWord] = i
                i += 1
            ans[i].append(word)
        '''
    