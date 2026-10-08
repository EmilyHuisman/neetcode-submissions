class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        while(len(heap) > 1):
            heapq.heapify(heap)
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, x-y)
        heap.append(0)
        return -(heapq.heappop(heap))
            



        