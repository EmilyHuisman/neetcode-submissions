class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # valid water flows:
            # High -> low
            # equal -> equal
            # cell -> ocean
        # goal: return all cells that have paths to pacific and atlantic

        # bfs grid 
        # we stop if weve reached pacific and atlantic
        
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()
        ans = []
        def dfs(r, c, visit, prevHeight):
            if min(r, c) < 0 or r==row or c==col or (r, c) in visit or prevHeight > heights[r][c]:
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row-1, c, atl, heights[row-1][c])
        
        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col-1, atl, heights[r][col-1])
        

        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        return ans



