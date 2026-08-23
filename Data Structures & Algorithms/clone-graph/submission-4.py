"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        head_copy = Node(node.val)
        visited = set()
        mapping = dict()
        mapping[node] = head_copy
        queue = deque()
        queue.append(node)
        while queue:
            og_node = queue.popleft()
            cp_node = mapping[og_node]
            visited.add(og_node)
            for neighbor in og_node.neighbors:
                if neighbor not in visited:
                    if neighbor not in mapping:
                        copy_neighbor = Node(neighbor.val, [cp_node])
                        mapping[neighbor] = copy_neighbor
                    else:
                        copy_neighbor = mapping[neighbor]
                        copy_neighbor.neighbors.append(cp_node)
                    cp_node.neighbors.append(copy_neighbor)
                    queue.append(neighbor)
        
        def print_nodes(node):
            visited = set()
            def dfs(node):
                visited.add(node)
                neighbor_vals = [node.val for node in node.neighbors]
                print(f"node: {node.val}, neighbours: {neighbor_vals}")
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        dfs(neighbor)
            dfs(node)

        print_nodes(node)
        print("copy:")
        print_nodes(head_copy)

        return head_copy
        