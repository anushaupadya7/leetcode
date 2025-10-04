# Last updated: 04/10/2025, 20:13:47
from typing import List
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # m=len(grid)
        # n=len(grid[0])
        # directions=[(0,1),(0,-1),(1,0),(-1,0)]

        # def dfs(sr,sc,r,c,visited,length):
        #     for dr,dc in directions:
        #         nr,nc=r+dr,c+dc
        #         if not (0 <= nr < m and 0 <= nc < n):
        #             continue
        #         if grid[nr][nc] != grid[sr][sc]:
        #             continue
        #         if (nr,nc) == (sr,sc) and length>=4:
        #             return True
        #         if (nr,nc) not in visited:
        #             visited.add((nr,nc))
        #             if dfs(sr,sc,nr,nc,visited,length+1):
        #                 return True
        #             visited.remove((nr,nc))
        #     return False


        # for i in range(m):
        #     for j in range(n):
        #         visited= set([(i, j)])
        #         if dfs(i,j,i,j,visited,1):
        #             return True
        # return False
        m, n = len(grid), len(grid[0])
        depth = [[0] * n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, d, pr, pc, char):
            depth[r][c] = d
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] != char:
                    continue
                if nr == pr and nc == pc:  # skip parent
                    continue
                if depth[nr][nc] == 0:     # unvisited
                    if dfs(nr, nc, d + 1, r, c, char):
                        return True
                else:
                    # back-edge → cycle exists
                    if d - depth[nr][nc] + 1 >= 4:
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if depth[i][j] == 0:  # new DFS
                    if dfs(i, j, 1, -1, -1, grid[i][j]):
                        return True
        return False
