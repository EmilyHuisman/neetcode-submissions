class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashset = {x: set() for x in range(9)}
        col_hashset = {x: set() for x in range(9)}
        box_hashmap = {(x, y): set() for x in range(3) for y in range(3)}

        for r in range(len(board)):
            for c in range(len(board[0])):
                box = ((r // 3), (c // 3))
                value = board[r][c]
                if value == ".":
                    continue
                if value in row_hashset[r] or value in col_hashset[c] or value in box_hashmap[box]:
                    return False
                row_hashset[r].add(value)
                col_hashset[c].add(value)
                box_hashmap[box].add(value)
        return True
        '''
        valid board:
            1. each row only contains digits 1-9 once
            2. each col only contains digits 1-9 once
            3. each 3x3 square only contains digits 1-9 once


        {0: (1, 2, None, None, 3, ...), 
         1: (4, None, None, 5, None, ...),
         3: }


         3 hashsets

        for which (r // 3) and (c//3)


         1. iterate over the board
            - calculate which box position is in
            - check whether value at index is in any of the 3 hashets
                - if yes: return False
                - if no: add value to all 3 sets
        - return True

        board[r][c] -> board[0][0] = 1
        

        row_hashset = set()
        col_hashset = set()
        box_hashmap = {(x, y) for x in range(3) and y in range(3)}

        for r in len(board):
            for c in len(board[0]):
                box = ((r // 3), (c // 3))
                value = board[r][c]
                if value in row_hashset or value in col_hashset or value in box_hashmap[box]:
                    return False
                row_hashset.add(value)
                col_hashset.add(value)
                board_hashmap[box].append(value)
        return True

        '''







