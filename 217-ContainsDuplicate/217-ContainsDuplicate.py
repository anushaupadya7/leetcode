# Last updated: 19/09/2025, 00:17:44
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # arr=set(nums)
        # if len(nums)==len(arr):
        #     return False 
        # else:
        #     return True
        seen={}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num]=1
        return False
