class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # perform dfs searching for if 
        # go thry array
        # chekcing if letter = first letter in the word
        # if yes: add to visited list
        # dfs: 
        # make sure in bounds
        # check if it equals letter
        # if yes move poinyter
        visited = []
        row, col = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if min(r, c) < 0 or r == row or c == col or (r, c) in visited or board[r][c] != word[i]:
                return False
            
            visited.append((r, c))
            i += 1
            res = dfs(r + 1, c, i) or dfs(r - 1, c, i) or dfs(r, c + 1, i) or dfs(r, c - 1, i)
            visited.remove((r, c))
            return res
            
            

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
    
        return False
