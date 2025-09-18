# Last updated: 19/09/2025, 00:16:30
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        sorted_queries=sorted(enumerate(queries),key=lambda x:x[1])

        result=[-1] * len(queries)

        min_heap=[]
        i=0
        for query_index,query in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                left,right=intervals[i]
                size=right-left+1
                heapq.heappush(min_heap,(size,right))
                i+=1

            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[query_index]=min_heap[0][0]
        return result



