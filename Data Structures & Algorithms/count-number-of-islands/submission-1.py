from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_height = len(grid)
        max_width = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        def bfs(node):
            queue = deque()
            queue.append(node)
            while queue:
                x, y = queue.popleft()
                visited.add((x,y))
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x >= max_width or \
                        new_y < 0 or new_y >= max_height:
                        continue
                    neighbour = (new_x, new_y)
                    if neighbour not in visited and grid[new_y][new_x] == "1":
                        queue.append(neighbour)

        # Attempt to do it with DFS, it works as well.
        def dfs(node):
            x, y = node
            visited.add(node)
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= max_width or \
                        new_y < 0 or new_y >= max_height:
                        continue
                neighbour = (new_x, new_y)
                if neighbour not in visited and grid[new_y][new_x] == "1":
                    dfs(neighbour)
        
        islands = 0
        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                if value == "1" and (x, y) not in visited:
                    islands += 1
                    dfs((x, y))
        return islands
                    