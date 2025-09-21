# Last updated: 22/09/2025, 00:22:57
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums,target):
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans

        def find_last(nums,target):
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
            

        return [find_first(nums,target),find_last(nums,target)]