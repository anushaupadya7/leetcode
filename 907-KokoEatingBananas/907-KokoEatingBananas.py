# Last updated: 19/09/2025, 00:16:49
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)

        while left<right:
            mid=(left+right)//2
            total_hours=sum(math.ceil(p/mid) for p in piles) 

            if total_hours > h: 
                left = mid + 1
            else:  
                right = mid

        return left 
