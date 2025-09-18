# Last updated: 19/09/2025, 00:16:57
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n=len(cost)
        if n==2:
            return min(cost[0],cost[1])

        prev2,prev1=cost[0],cost[1]

        for i in range(2,n):
            curr=cost[i]+min(prev1,prev2)
            prev2=prev1
            prev1=curr
        return min(prev1,prev2)