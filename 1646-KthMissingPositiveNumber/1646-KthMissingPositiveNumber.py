# Last updated: 25/09/2025, 00:21:13
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low=0
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2
            if arr[mid]-(mid+1)<k:
                low=mid+1
            else:
                high=mid-1
        
        return high+1+k