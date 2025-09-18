# Last updated: 19/09/2025, 00:17:52
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() 
    
        while n != 1:
            if n in seen:
                return False  
            
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return True
