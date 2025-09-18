# Last updated: 19/09/2025, 00:18:48
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        columns=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num=board[i][j]

                if num == ".":
                    continue

                board_index=(i//3)*3+(j//3)
                
                if num in rows[i] or num in columns[j] or num in box[board_index]:
                    return False

                rows[i].add(num)
                columns[j].add(num)
                box[board_index].add(num)
                print(rows)

        return True

