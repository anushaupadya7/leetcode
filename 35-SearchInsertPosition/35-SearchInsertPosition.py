# Last updated: 23/09/2025, 17:52:57
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        ans=0
        while low<=high:
            mid=(low+high)//2
            if nums[mid] < target:
                ans=mid+1
                low=mid+1
            else:
                high=mid-1

        return ans