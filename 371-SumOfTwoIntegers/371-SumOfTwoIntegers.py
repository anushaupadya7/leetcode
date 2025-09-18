# Last updated: 19/09/2025, 00:17:24
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return a+b
        MASK=0xFFFFFFFF
        INT_MAX=0x7FFFFFFF

        while b!=0:
            carry=(a&b)<<1
            a=(a^b) & MASK
            b=carry & MASK
        return a if a<=INT_MAX else ~(a^MASK)
