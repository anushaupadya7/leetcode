# Last updated: 19/09/2025, 00:17:10
import heapq
from collections import Counter,deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        max_heap=[-count for count in count.values()]
        heapq.heapify(max_heap)

        queue=deque()
        time=0

        while max_heap or queue:
            time+=1

            if max_heap:
                task=heapq.heappop(max_heap) + 1
                if task:
                    queue.append((task,time+n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap,queue.popleft()[0])
            
        return time