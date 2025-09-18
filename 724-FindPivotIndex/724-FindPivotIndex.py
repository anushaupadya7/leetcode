# Last updated: 19/09/2025, 00:17:00
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum=0

        for i,num in enumerate(nums):
            if left_sum * 2 + nums[i] == total_sum:
                return i
            left_sum+=num
        
        return -1