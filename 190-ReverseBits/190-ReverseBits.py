# Last updated: 19/09/2025, 00:17:58
class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for i in range(32):
            last_bit=n&1
            result= (result<<1) | last_bit
            n=n>>1
        
        return result

        