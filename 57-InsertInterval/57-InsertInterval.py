# Last updated: 19/09/2025, 00:18:35
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        for interval in intervals:
            if interval[1]<newInterval[0]:
                result.append(interval)

            elif interval[0] > newInterval[1]:  
                result.append(newInterval)
                newInterval = interval 
            
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        result.append(newInterval)
        
        return result

        