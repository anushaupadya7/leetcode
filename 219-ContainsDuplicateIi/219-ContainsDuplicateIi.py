# Last updated: 19/09/2025, 00:17:43
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index={}

        for i,num in enumerate(nums):
            if num in num_index and i-num_index[num]<=k:
                return True
            else:
                num_index[num]=i
        return False
