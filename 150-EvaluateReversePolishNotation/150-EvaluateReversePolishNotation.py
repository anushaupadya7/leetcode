# Last updated: 19/09/2025, 00:18:07
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()  
                a = stack.pop()  
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
    
        return stack[0]