class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        # we know weve reached an island when all directions
        # lead to zero, assuming we started at 1
        count = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >=row or c>=col or grid[r][c] == '0':
                return
            
            if grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1) 

        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c] == '1':
                    count+= 1
                    dfs(r, c)
        return count   