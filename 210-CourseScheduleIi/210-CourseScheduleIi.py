# Last updated: 19/09/2025, 00:17:49
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(numCourses)}

        order=[]
        cycle=False

        for course,prereq in prerequisites :
            graph[prereq].append(course)
        
        visited=[0]*numCourses

        def dfs(course):
            nonlocal cycle
            if visited[course]==1:
                cycle=True
                return
            if visited[course]==2:
                return
            visited[course]=1
            for neighbour in graph[course]:
                dfs(neighbour)
            visited[course]=2
            order.append(course)
            


        for i in range(numCourses):
            if visited[i]==0:
                dfs(i)

        if cycle:
            return []

        return order[::-1]
