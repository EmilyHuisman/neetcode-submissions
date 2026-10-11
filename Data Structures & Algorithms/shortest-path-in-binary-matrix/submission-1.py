class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # n by n matrix (grid)
        # goal: return the shorest clear path
            # move in all directions (including diagonally)
        # return -1 if no path found
        # start 0, 0 end is n-1, n-1

        row, col = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1


        length = 1
        while queue:
            for i in range(len(queue)):
                # pop from the queue
                # check base case if it reached the end
                r, c = queue.popleft()
                if r == row - 1 and c == col-1:
                    return length
                
                # if not were going to check suroudning verticies
                # check base cases for those (bounds, in visited, if it equals 1)
                neighboors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
                for nr, nc in neighboors:
                    if (min(nr + r, nc + c) < 0 or nr + r >= row or nc + c >= col or (nr+r, nc+c) in visited or grid[nr+r][nc+c] == 1):
                        continue
                # else:
                    # add it to the queue
                    # add it to visited
                    queue.append((nr+r, nc+c))
                    visited.add((nr+r, nc+c))

                # increase length
            length += 1
        return -1


        