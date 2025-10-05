# Last updated: 05/10/2025, 15:56:55
class Solution:
    def fib(self, n: int) -> int:
        # if n<=1:
        #     return n

        # return self.fib(n-1)+self.fib(n-2)

        # dp=[0]*(n+1)
        # print(dp)
        # if n<=1:
        #     return n

        # dp[1]=1

        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]

        # return dp[n] 

        if n<=1:
            return n
        
        a,b=0,1

        for _ in range(2,n+1):
            a,b=b,a+b

        return b