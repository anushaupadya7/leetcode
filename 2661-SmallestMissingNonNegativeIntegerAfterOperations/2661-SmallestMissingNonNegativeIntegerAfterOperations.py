# Last updated: 16/10/2025, 23:00:34
from collections import Counter
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainders = []

        for num in nums:
            remainder = (num % value + value) % value 
            remainders.append(remainder)

        print(remainders)

        remainder_count = Counter(remainders)

        mex = 0
        while True:
            mod = mex % value
            if remainder_count[mod] > 0:
                remainder_count[mod] -= 1
                mex += 1
            else:
                return mex
