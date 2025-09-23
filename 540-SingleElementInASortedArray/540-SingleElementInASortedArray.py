# Last updated: 23/09/2025, 17:51:33
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1

        while low<high:
            mid=(low+high)//2

            if mid%2 == 1:
                mid-=1
            
            if nums[mid]==nums[mid+1]:
                low=mid+2
            else:
                high=mid
        return nums[low]