# Last updated: 19/09/2025, 00:17:47
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        # 0,n-1
        # 1,n-2
        def houseRob(nums):
            prev2, prev1 = 0, 0
            for num in nums:
                curr = max(prev1, num + prev2)
                prev2, prev1 = prev1, curr
            return prev1
        return max(houseRob(nums[:-1]), houseRob(nums[1:]))
