# Last updated: 26/09/2025, 23:14:52
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left=min(bloomDay)
        right=max(bloomDay)
        result=0

        if len(bloomDay)<m*k:
            return -1

        def can_make_boquets(day):
            flowers=0
            bouquets=0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0
                else:
                    flowers=0
                    
            if bouquets>=m:
                return True

            return bouquets>=m
        
        while left<=right:
            mid=(left+right)//2

            if can_make_boquets(mid):
                result=mid
                right=mid-1
            else:
                left=mid+1

        return result