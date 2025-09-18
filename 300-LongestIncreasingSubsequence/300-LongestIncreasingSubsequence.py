# Last updated: 19/09/2025, 00:17:30
from functools import lru_cache
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1] * n
        
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)
        sub=[]
        for num in nums:
            i=bisect.bisect_left(sub,num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i]=num
        return len(sub)

        