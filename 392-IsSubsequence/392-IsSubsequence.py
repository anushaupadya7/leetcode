# Last updated: 19/09/2025, 00:17:22
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0 
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  
                i += 1
            j += 1 
        
        return i == len(s)  
