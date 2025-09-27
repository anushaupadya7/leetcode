# Last updated: 28/09/2025, 00:56:59
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
       
        def canCarry(weight):
            current_day=1
            current_load = 0
            for w in weights:
                if current_load+w<=weight:
                    current_load += w
                else:
                    current_day += 1
                    current_load = w
                    if current_day > days:
                        return False
            return True

        while left<=right:
            mid=(left+right)//2
            if canCarry(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans













        # brute force
        # left=max(weights)
        # right=sum(weights)
       
        # def canCarry(weight):
        #     current_day=1
        #     current_load = 0
        #     for w in weights:
        #         if current_load+w<=weight:
        #             current_load += w
        #         else:
        #             current_day += 1
        #             current_load = w
        #             if current_day > days:
        #                 return False
        #     return True

        # for weight in range(left,right+1):
        #     if canCarry(weight):
        #         return weight

   
            


