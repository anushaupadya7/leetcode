# Last updated: 19/09/2025, 00:16:31
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=[]
        i,j=0,0

        while i<len(word1) and j<len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i=i+1
            j=j+1
        
        merged.append(word1[i:])
        merged.append(word2[j:])

        return "".join(merged)