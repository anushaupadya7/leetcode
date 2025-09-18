# Last updated: 19/09/2025, 00:17:31
import heapq

class MedianFinder:
    def __init__(self):
        self.low = [] 
        self.high = []  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)

        if self.low and self.high and (-self.low[0] > self.high[0]):
            heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0] 
        return (-self.low[0] + self.high[0]) / 2 


