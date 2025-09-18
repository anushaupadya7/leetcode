# Last updated: 19/09/2025, 00:18:01
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:  
                left = mid + 1
            else:
                right = mid  

        return left  
   