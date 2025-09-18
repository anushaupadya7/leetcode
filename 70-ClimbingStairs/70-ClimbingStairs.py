# Last updated: 19/09/2025, 00:18:33
class Solution:
    def climbStairs(self, n: int) -> int:
        # bruteforce 0(2^n)
        # if n<=1:
        #     return 1
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        
        # memo={}
        # if n in memo:
        #     return memo[n]
        # if n<=1:
        #     return 1
        # memo[n]=self.climbStairs(n-1)+self.climbStairs(n-2)

        # return memo[n]

        if n<=1:
            return 1
        
        prev1,prev2=1,1
        for _ in range(2,n+1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        return prev1





