# Last updated: 19/09/2025, 00:18:04
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = res = nums[0]

        for i in range(1,len(nums)):
            curr=nums[i]

            if curr<0:
                max_prod,min_prod = min_prod,max_prod

            max_prod=max(curr,curr*max_prod)
            min_prod=min(curr,curr*min_prod)

            res=max(res,max_prod)

        return res
