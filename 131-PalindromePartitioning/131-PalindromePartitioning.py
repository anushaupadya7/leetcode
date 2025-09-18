# Last updated: 19/09/2025, 00:18:14
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()
                    
        backtrack(0, [])
        return res
