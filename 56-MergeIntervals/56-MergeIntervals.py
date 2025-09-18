# Last updated: 19/09/2025, 00:18:37
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged=[]
        intervals.sort(key=lambda x:x[0])
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1], interval[1])
        return merged