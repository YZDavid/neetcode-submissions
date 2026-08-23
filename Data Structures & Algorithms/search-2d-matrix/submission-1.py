class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # Binary search which row to look for
        top, bot = 0, ROWS - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            # If the target is smaller than the row's first value,
            # it is not there and possibly in an earlier row
            if target < matrix[mid_row][0]:
                bot = mid_row - 1
            # If the target is larger than the row's last value,
            # it is not there and possibly in a later row
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            # If neither (meaning within the row, select this row)
            else:
                selected_row_idx = mid_row
                break
        
        # If loop broke not because of selected row
        if top > bot:
            return False
        selected_row_idx = (top + bot) // 2
        # Now, standard Binary Search problem
        selected_row = matrix[selected_row_idx]
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target < selected_row[m]:
                r = m - 1
            elif target > selected_row[m]:
                l = m + 1
            else:
                return True
        
        return False
            