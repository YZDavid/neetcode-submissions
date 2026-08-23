class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum_area = 0
        movement = ((1,0), (0,1), (-1,0), (0,-1))
        max_row = len(grid)
        max_col = len(grid[0])
        visited = set()
        # node format - (r, c)
        def dfs(node, size):
            visited.add(node)
            size += 1
            for r_delta, c_delta in movement:
                new_r = node[0] + r_delta
                new_c = node[1] + c_delta
                new_node = (new_r, new_c)
                row_check = new_r >= 0 and new_r < max_row
                col_check = new_c >= 0 and new_c < max_col
                visited_check = new_node not in visited
                if row_check and col_check and visited_check:
                    if grid[new_r][new_c]:
                        size = dfs(new_node, size)
            return size
            
        
        for r in range(max_row):
            for c in range(max_col):
                node = (r, c)
                if node not in visited and grid[r][c]:
                    size = dfs(node, 0)
                    maximum_area = max(maximum_area, size)
        
        return maximum_area
                