# Last updated: 9/18/2025, 11:53:46 PM
class Solution:
    def minimumSteps(self, s: str) -> int:
        black_count=0
        result=0
        for i in range(len(s)):
            if s[i]=='1':
                black_count+=1
            if s[i]=='0':
                result+=black_count
        return result
