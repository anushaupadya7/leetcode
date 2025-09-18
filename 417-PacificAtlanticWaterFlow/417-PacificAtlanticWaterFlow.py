# Last updated: 19/09/2025, 00:17:19
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])

        pacific=set()
        atlantic=set()

        def dfs(r,c,visited,prevHeight):
            if (r,c) in visited or r<0 or r>=m or c<0 or c>=n or heights[r][c]<prevHeight:
                return
            visited.add((r,c))
            directions=[(0,1),(0,-1),(1,0),(-1,0)]

            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])


        for i in range(m):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,n-1,atlantic,heights[i][n-1])

        for j in range(n):
            dfs(0,j,pacific,heights[0][j])
            dfs(m-1,j,atlantic,heights[m-1][j])

        return list(pacific & atlantic)