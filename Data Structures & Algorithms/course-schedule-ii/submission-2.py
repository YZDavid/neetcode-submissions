class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = dict()
        # Populate adjacency list
        for course in range(numCourses):
            adjacency_list[course] = []
        for a, b in prerequisites:
            adjacency_list[b].append(a)
        
        course_stack = []
        visited = [0] * numCourses
        cycle = []

        print(adjacency_list)
        def dfs(course):
            print(course)
            visited[course] = 1
            print(visited)
            for neighbour in adjacency_list[course]:
                if visited[neighbour] == 1:
                    print("cycle detected")
                    cycle.append(True)
                    return
                dfs(neighbour)
            course_stack.append(course)
            print(course_stack)
            visited[course] = 2
        
        for course in range(numCourses):
            if visited[course] == 0:
                dfs(course)
                if cycle:
                    return []

        course_stack.reverse()
        return course_stack