class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap key represents freq on letter
        # value is word
        
        # loop thru list and add words to hashmap
        # return the values in a list

        hashMap = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for c in word:
                index = (ord(c) - ord('a'))
                arr[index] += 1
            hashMap[tuple(arr)].append(word) # have to make it a tuple bc keys must be hashable
            # tuple = immutable --> hashable which keep needs
        
        return list(hashMap.values()) # cast as a list since .values() returns dict_values object





