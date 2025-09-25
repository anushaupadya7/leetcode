# Last updated: 26/09/2025, 00:01:28
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1

























        # left=0
        # right=len(nums)-1

        # while left<=right:
        #     mid=(left+right)//2

        #     if nums[mid]==target:
        #         return mid
        #     if nums[left]<=nums[mid]:
        #         if nums[left]<=target<nums[mid]:
        #             right=mid-1
        #         else:
        #             left=mid+1

        #     else:
        #         if nums[mid]<target<=nums[right]:
        #             left=mid+1
        #         else:
        #             right=mid-1

        # return -1