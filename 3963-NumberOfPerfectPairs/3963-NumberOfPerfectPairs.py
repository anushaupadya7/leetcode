# Last updated: 9/18/2025, 11:53:48 PM
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        # n=len(nums)
        # ans=0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         a,b=nums[i],nums[j]
        #         cond1=min(abs(a-b),abs(a+b))<=min(abs(a),abs(b))
        #         cond2=max(abs(a-b),abs(a+b))>=max(abs(a),abs(b))
        #         if cond1 and cond2:
        #             ans+=1

        # return ans

        arr=sorted(abs(x) for x in nums)
        n=len(nums)
        ans=0

        for i,x in enumerate(arr):
            lo=bisect_left(arr,(x+1)//2)
            hi=bisect_right(arr,(2*x))-1

            if hi>i:
                ans+=hi-max(lo,i+1) + 1

        return ans