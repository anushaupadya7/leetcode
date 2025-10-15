# Last updated: 15/10/2025, 21:02:37
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        # left
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = left[i - 1] + 1

        # right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = right[i + 1] + 1

        max_k = 0
        for i in range(n - 1):
            max_k = max(max_k, min(left[i], right[i + 1]))

        return max_k
