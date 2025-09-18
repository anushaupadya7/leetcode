# Last updated: 19/09/2025, 00:16:44
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        minutes=0
        fresh_count=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                if grid[r][c]==1:
                    fresh_count+=1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]  
        while queue:
            dx,dy,minutes=queue.popleft()
            for x,y in directions:
                nx=x+dx
                ny=y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                    grid[nx][ny]=2
                    queue.append((nx,ny,minutes+1))
                    fresh_count-=1
        return minutes if fresh_count==0 else -1
            


   
            