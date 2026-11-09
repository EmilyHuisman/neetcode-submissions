class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visit = set()
        heap = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        

        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (rows-1, cols-1):
                return effort
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) in visit:
                    continue
                
                new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap, (new_effort, nr, nc))
        return 0
                





