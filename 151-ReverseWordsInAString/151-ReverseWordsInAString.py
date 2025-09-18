# Last updated: 19/09/2025, 00:18:06
class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(s.split()[::-1])
        res, word = [], []
        for char in s:
            if char != ' ':
                word.append(char)  
            elif word:
                res.append("".join(word)) 
                word = []  

        if word:
            res.append("".join(word))  
        
        return " ".join(res[::-1]) 
