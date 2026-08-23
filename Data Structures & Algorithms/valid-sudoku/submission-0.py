class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        grid_set = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val == ".":
                    continue
                grid_row = row // 3
                grid_col = col // 3
                if (val in row_set[row] or 
                    val in col_set[col] or
                    val in grid_set[grid_row][grid_col]):
                    return False
                row_set[row].add(val)
                col_set[col].add(val)
                grid_set[grid_row][grid_col].add(val)
        
        return True
                    

                