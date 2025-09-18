# Last updated: 19/09/2025, 00:17:18
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=Counter()
        l=0
        max_freq=0
        res=0
        
        for r in range(len(s)):
            freq[s[r]]+=1
            max_freq=max(max_freq,freq[s[r]])

            while (r-l+1)-max_freq>k:
                freq[s[l]]-=1
                l+=1
            
            res=max(res,r-l+1)

        return res