class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # have a hashmap that will stores: word, index
        # loop through the list and create sorted word
        # agasinst hash map check if sroted word exists, if no add to hash map
        # if yes add to list

        ans = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                index = (ord(c)-ord('a'))
                count[index] += 1
            ans[tuple(count)].append(word)
        return list(ans.values())

    