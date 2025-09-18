# Last updated: 19/09/2025, 00:16:24
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        freq=Counter()
        max_freq=0
        l=0
        res=0

        for r in range(len(nums)):
            freq[nums[r]]+=1
            max_freq=max(max_freq,freq[nums[r]])

            while (r-l+1)-max_freq>k:
                freq[nums[l]]-=1
                l+=1
            
            res=max(res,max_freq)

        return res
