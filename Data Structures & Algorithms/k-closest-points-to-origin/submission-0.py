class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        * priority heap of size k

        - iterate thru list
        - for each point
            - calculate distance
            - push onto max heap if value is less than node (pop original node first)
            - heapify
            - put distance as key-value pair (distnace, point) in a hashset
        - pop heap, searching hashset for values and appending to answer



        * priority heap of size k (max heap)

        - iterate thru list
        - for each point
            - calculate distance from origin
            - push point to heap (tuple: distance, x, y)
            - if size of heap is larger than k pop
        - return the x y cordinates in a list

        '''
        maxHeap = []
        for x, y in points:
            distance = -(x**2 + y**2)

            heapq.heappush(maxHeap, (distance, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [[x, y] for _, x, y, in maxHeap]

