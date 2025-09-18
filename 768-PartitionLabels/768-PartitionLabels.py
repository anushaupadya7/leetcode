# Last updated: 19/09/2025, 00:16:56
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}

        for i,char in enumerate(s):
            last[char]=i
        
        start=end=0
        result=[]

        for i,char in enumerate(s):
            end=max(end,last[char])
            if i==end:
                result.append(end - start + 1)  
                start = i + 1 

        return result