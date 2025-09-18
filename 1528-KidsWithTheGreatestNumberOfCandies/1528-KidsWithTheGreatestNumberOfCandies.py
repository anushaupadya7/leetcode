# Last updated: 19/09/2025, 00:16:38
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [(candy + extraCandies) >= max_candies for candy in candies]