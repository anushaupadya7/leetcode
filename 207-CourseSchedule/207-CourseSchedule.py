# Last updated: 19/09/2025, 00:17:50
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}

        for prereq,courses in prerequisites:
            graph[courses].append(prereq)

        visited=[0]*numCourses

        def dfs(course):
            if visited[course]==1:
                return False
            if visited[course]==2:
                return True

            visited[course]=1
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            visited[course]=2
            return True



        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

        