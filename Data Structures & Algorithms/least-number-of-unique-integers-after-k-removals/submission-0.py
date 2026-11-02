class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        '''
        Given: an array of ints, k = # of elements to remove
        Goal: return smallest number of distinct int values

        * removing an element only removes that occurence

        k = 2
        [1,1,2,3]
        
        1: 2
        2: 1
        3: 1

        create a hashmap that has the counts
        delete the elements up to k with the lowest counts

        1. countign the frequencies
        2. bucketsort
        3. delete the k smallest variables
        4. return the variables after that

        '''    


        frequencies = Counter(arr)
        

        bucketFreq = [[] for _ in range(len(arr) +1)]

        for num, freq in frequencies.items():
            bucketFreq[freq].append(num)
        
        unique = len(frequencies)
        for freq in range(1, len(bucketFreq)):
            for num in bucketFreq[freq]:
                if k >= freq:
                    k -= freq
                    unique -=1
                else:
                    return unique
        return unique




         












