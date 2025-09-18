# Last updated: 19/09/2025, 00:17:05
from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos=bisect_left(arr,x)
        left=pos-1
        right=pos
        n=len(arr)

        while k>0:
            if left<0:
                right+=1
            elif right>=n:
                left-=1
            elif abs(arr[left]-x)<=abs(arr[right]-x):
                left-=1
            else:
                right+=1
            k-=1
        return arr[left+1:right]

            

        