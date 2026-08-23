class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = dict()
        # Populate adjacency list
        for course in range(numCourses):
            adjacency_list[course] = []
        for a, b in prerequisites:
            adjacency_list[b].append(a)
        
        visited = [0] * numCourses
        def dfs(course):
            visited[course] = 1
            status = True
            for neighbour in adjacency_list[course]:
                if visited[neighbour] == 1:
                    return False
                status = status and dfs(neighbour)
            visited[course] = 2
            return status
        
        for course in range(numCourses):
            if visited[course] == 0:
                cycle = not dfs(course)
                if cycle:
                    return False
        return True
                
        
        
