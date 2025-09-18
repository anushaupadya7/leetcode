# Last updated: 19/09/2025, 00:18:32
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return None

        m=len(matrix)
        n=len(matrix[0])

        left=0
        right=m*n-1

        while left<=right:
            mid=(left+right)//2
            row=mid//n
            column=mid%n

            if matrix[row][column] == target:
                return True
            elif  matrix[row][column] < target:
                left=mid+1
            else:
                right=mid-1
        return False
