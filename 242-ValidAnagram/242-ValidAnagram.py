# Last updated: 19/09/2025, 00:17:36
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)

        # return Counter(s)==Counter(t)

        # if len(s) != len(t):
        #     return False
        
        # count=defaultdict(int)

        # for char in s:
        #     count[char]+=1

        # for char in t:
        #     count[char]-=1
        #     if count[char]<0:
        #         return False

        # return True

        if len(s)!=len(t):
            return False

        count=[0]*26
        
        for char in s:
            count[ord(char)-ord('a')]+=1

        for char in t:
            count[ord(char)-ord('a')]-=1

        return all(x==0 for x in count)


