# Last updated: 28/09/2025, 23:15:49
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer={
            "I": 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        n=len(s)
        ans=0

        for i in range(n):
            if i<n-1 and roman_to_integer[s[i]]<roman_to_integer[s[i+1]]:
                ans-=roman_to_integer[s[i]]
            else:
                ans+=roman_to_integer[s[i]]
        
        return ans
