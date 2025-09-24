# Last updated: 24/09/2025, 22:51:14
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low = 1
        high = x // 2

        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
