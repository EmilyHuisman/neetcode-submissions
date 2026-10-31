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
        #10/30
        # time complexity: O(nlogk) where n is len(nums)
        # space complexity O(k) 
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]










