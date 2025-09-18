# Last updated: 19/09/2025, 00:16:34
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={"a","e","i","o","u"}
        curr_vowels=0
        max_vowels=0

        for i in range(k):
            if s[i] in vowels:
                curr_vowels+=1

        max_vowels=curr_vowels

        for i in range(k,len(s)):
            if s[i] in vowels:
                curr_vowels+=1
            if s[i-k] in vowels:
                curr_vowels-=1
            max_vowels=max(max_vowels,curr_vowels)

            if max_vowels == k:  
                return k

        return max_vowels
            
        
        