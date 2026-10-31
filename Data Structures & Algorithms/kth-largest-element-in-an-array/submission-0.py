class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        min heap of size k
        push elements to heap
        

        goal: return the kth largest element
        Given: unsorted array, k


        *  min heap

        1. iterate thru nums
            - push onto heap
            if heap > k:
                pop root node (min)
        
        return root node - kth largest element
        '''


        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heapq.heappop(heap)










