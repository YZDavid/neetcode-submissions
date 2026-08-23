class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Less than or equal Binary Search
        def leq_bs(lst, target):
            # Will return a tuple of boolean and integer
            # to keep track of exact or approximate match
            l, r = 0, len(lst) - 1
            while l <= r:
                m = l + (r - l) // 2
                if lst[m] > target:
                    r = m - 1
                elif lst[m] < target:
                    l = m + 1
                else:
                    return (True, m)
            return (False, l - 1)
        
        first_column_lst = [row[0] for row in matrix]
        approx, row_index = leq_bs(first_column_lst, target)
        if approx:
            return True
        if row_index < 0:
            return False
        
        row = matrix[row_index]
        a, b = leq_bs(row, target)
        return a

            
