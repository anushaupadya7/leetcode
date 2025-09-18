# Last updated: 9/18/2025, 6:17:43 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found={}
        for i,num in enumerate(nums):
            if num in found: 
                return [found[num],i]
            else:
                complement=target-num
                found[complement]=i
        return []

        