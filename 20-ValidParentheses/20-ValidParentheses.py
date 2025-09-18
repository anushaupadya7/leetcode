# Last updated: 19/09/2025, 00:18:52
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map={'}':'{',']':'[',')':'('}
        for char in s:
            if char in bracket_map:
                top=stack.pop() if stack else '#'

                if top!=bracket_map[char]:
                    return False

            else:
                stack.append(char)
        return not stack
