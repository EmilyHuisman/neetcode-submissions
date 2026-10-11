class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:  
        # loop thru the grid to find the positionsof the rotten fruit
        # add rotten fruit to queue
        row, col = len(grid), len(grid[0])
        queue = deque()
        freshOranges = 0
        minutes = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    freshOranges += 1


                    
    
        # bfs of grid starting from the queue
        # first check if queue is empty, immediatly return -1
        
        # loop thru the queue
        # pop rotten fruit
            # check each direction (L, R, D, U)
            # if it equals 1, change value to 2
        # update minute count
        # return minute count
        while queue and freshOranges > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                neighboors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                
                for nr, nc in neighboors:
                    if min(nr+r, nc+c) >= 0 and nr+r < row and nc +c < col and grid[nr+r][nc+c] == 1:
                        grid[nr+r][nc+c] = 2
                        freshOranges -= 1
                        queue.append((nr+r, nc+c))
            minutes += 1
        if freshOranges == 0:
            return minutes
        
     
        return -1








