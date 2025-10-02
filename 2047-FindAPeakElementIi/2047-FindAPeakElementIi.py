# Last updated: 02/10/2025, 21:59:40
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])

        left=0
        right=n-1

        maxRow=0

        while left<=right:
            mid=(left+right)//2

            for i in range(m):
                if mat[i][mid]>mat[maxRow][mid]:
                    maxRow=i

            leftVal = mat[maxRow][mid-1] if mid-1>=0 else -1
            rightVal = mat[maxRow][mid+1] if mid+1<n else -1
            currVal = mat[maxRow][mid]
            
            if currVal >= leftVal and currVal >= rightVal:
                return [maxRow, mid]
            elif leftVal > currVal:
                right = mid - 1
            else:
                left = mid + 1
