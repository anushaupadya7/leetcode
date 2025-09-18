# Last updated: 19/09/2025, 00:16:23
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()  
            else:
                stack.append(char)  
        
        return ''.join(stack) 
