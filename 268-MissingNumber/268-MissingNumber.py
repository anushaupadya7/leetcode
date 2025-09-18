# Last updated: 19/09/2025, 00:17:35
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing=len(nums)
        for i,num in enumerate(nums):
            missing=missing^i^num
        return missing