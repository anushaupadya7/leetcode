# Last updated: 19/09/2025, 00:18:39
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=nums[0]
        max_sum=nums[0]

        for i in range(1,len(nums)):
            current_sum=max(nums[i],current_sum + nums[i])
            max_sum=max(current_sum,max_sum)
        return max_sum

        
       



