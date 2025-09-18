# Last updated: 19/09/2025, 00:18:38
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump=0

        for i in range(len(nums)):
            if i>max_jump:
                return False

            max_jump=max(max_jump,i+nums[i])

            if max_jump>=len(nums)-1:
                return True
            
