# Last updated: 19/09/2025, 00:18:43
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)

        if n==1:
            return 0

        jumps=0
        end=0
        farthest=0

        for i in range(n-1):
            farthest=max(farthest,i+nums[i])
            # if i<end:
            #     continue
            if i==end:
                jumps+=1
                end=farthest
                if end >= n - 1:  
                    break
        return jumps
