# Last updated: 19/09/2025, 00:18:16
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # "X","X","X","X"
        # "X","O","O","X"
        # "X","X","O","X"
        # "X","O","X","X"

        # "X","X","X","X"
        # "X","X","X","X"
        # "X","X","X","X"
        # "X","O","X","X"

        rows=len(board)
        cols=len(board[0])

        def dfs(r,c):
            if 0<=r<rows and 0<=c<cols and board[r][c]=='O':
                board[r][c]='T'
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    dfs(r+dr,c+dc)

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][cols-1] == 'O':
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[rows-1][c] == 'O':
                dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                if board[r][c]=='T':
                    board[r][c]='O'
                



        