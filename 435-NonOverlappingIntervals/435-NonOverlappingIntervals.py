# Last updated: 19/09/2025, 00:17:16
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        # 1,2    1,3   2,3   3,4

        remove=0
        endInterval=float('-inf')
        print(endInterval)

        for start,end in intervals:
            if start<endInterval:
                remove+=1
            else:
                endInterval=end
        return remove

