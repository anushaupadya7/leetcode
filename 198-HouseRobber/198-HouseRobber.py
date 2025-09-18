# Last updated: 19/09/2025, 00:17:56
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]
        
        prev2,prev1=0,nums[0]

        for i in range(1,n):
            curr=max(prev1,nums[i]+prev2)
            prev2=prev1
            prev1=curr

        return curr
        # return prev1 - both have same value
        