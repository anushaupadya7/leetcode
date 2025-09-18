# Last updated: 19/09/2025, 00:16:36
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        window_size=n-k
        total_sum=sum(cardPoints)

        min_window_sum=sum(cardPoints[:window_size])
        current_sum=min_window_sum

        for i in range(window_size,n):
            current_sum+=cardPoints[i]-cardPoints[i-window_size]
            min_window_sum=min(min_window_sum,current_sum)

        return total_sum-min_window_sum
