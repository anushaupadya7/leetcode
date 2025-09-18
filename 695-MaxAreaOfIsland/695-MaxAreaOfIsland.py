# Last updated: 19/09/2025, 00:17:01
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows=len(grid)
        cols=len(grid[0])

        max_area=0

        # def dfs(r,c):
        #     if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
        #         return 0
        #     grid[r][c]=0
        #     area=1

        #     area+=dfs(r+1,c)
        #     area+=dfs(r-1,c)
        #     area+=dfs(r,c+1)
        #     area+=dfs(r,c-1)

        #     return area

        def bfs(r,c):
            queue=deque([(r,c)])
            grid[r][c]=0
            area=1

            directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                x,y=queue.popleft()

                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                        queue.append((nx, ny))
                        grid[nx][ny]=0
                        area+=1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    max_area=max(bfs(r,c),max_area)
        
        return max_area
