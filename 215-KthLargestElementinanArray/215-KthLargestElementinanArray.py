# Last updated: 03/10/2025, 16:20:23
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]

        for num in nums:
            heapq.heappush(min_heap,num)

            if (len(min_heap)>k):
                heapq.heappop(min_heap)

        return min_heap[0] if min_heap else -1
