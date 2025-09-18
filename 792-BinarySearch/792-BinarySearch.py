# Last updated: 19/09/2025, 00:16:54
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i,num in enumerate(nums):
        #     if num == target:
        #         return i
        # return -1

        low=0
        high=len(nums)-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
