# Last updated: 19/09/2025, 00:17:54
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count=0
        if not grid:
            return 0
        
        rows=len(grid)
        cols=len(grid[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0":
                return 
            grid[r][c]="0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    dfs(r,c)
                    island_count+=1
        return island_count


        # def bfs(r, c):
        #     queue = deque([(r, c)])
        #     grid[r][c] = "0"

        #     while queue:
        #         x, y = queue.popleft()
        #         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #             nx, ny = x + dx, y + dy
        #             if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
        #                 queue.append((nx, ny))
        #                 grid[nx][ny] = "0"
