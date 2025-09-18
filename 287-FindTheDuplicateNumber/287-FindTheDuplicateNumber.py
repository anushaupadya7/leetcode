# Last updated: 19/09/2025, 00:17:32
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # for num in nums:
        #     if num in seen: 
        #         return num
        #     seen.add(num) 
        slow,fast=nums[0],nums[nums[0]]

        while slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]

        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow

