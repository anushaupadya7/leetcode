# Last updated: 23/10/2025, 23:36:14
class Solution:
    def hasSameDigits(self, s: str) -> bool:
       
        
        while len(s)>2:
            res=""
            for i in range(len(s)-1):
                val=(int(s[i])+int(s[i+1]))%10
                res+=str(val)
            s=res

       
         

        return s[0]==s[1]
            

