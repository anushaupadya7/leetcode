# Last updated: 19/09/2025, 00:17:57
class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        bit_val=bin(n)
        bit_value=bit_val[2:]
        count=0
        for val in bit_value:
            if val=="1":
                count+=1
        return count
        