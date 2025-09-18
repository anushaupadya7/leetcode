# Last updated: 19/09/2025, 00:19:00
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def calculatePalindrome(l:int,r:int) -> str:
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        longest=""
        for i in range(len(s)):
            # odd length
            odd_length=calculatePalindrome(i,i)
            if len(odd_length)>len(longest):
                longest=odd_length

            # even length
            even_length=calculatePalindrome(i,i+1)
            if len(even_length)>len(longest):
                longest=even_length

        return longest

