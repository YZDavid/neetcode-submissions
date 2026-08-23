class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        initial_letter = word[0]
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def dfs(coordinate, letter_idx, visited):
            if letter_idx == len(word):
                return True
            x, y = coordinate
            if x < 0 or x >= len(board[0]) \
            or y < 0 or y >= len(board) \
            or coordinate in visited \
            or board[y][x] != word[letter_idx]:
                return False
            visited.add(coordinate)
            res = False
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                res = res or dfs((new_x, new_y), letter_idx + 1, visited)
            visited.remove(coordinate)
            return res 
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                letter = board[y][x]
                if letter == initial_letter:
                    outcome = dfs((x, y), 0, set())
                    if outcome:
                        return True
        return False

                