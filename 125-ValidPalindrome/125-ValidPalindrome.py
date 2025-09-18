# Last updated: 19/09/2025, 00:18:18
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        while i<j : 
            if not s[i].isalnum():
                i+=1 
            elif not s[j].isalnum():
                j-=1
        
            elif(s[i].isalnum() and s[j].isalnum() and s[i].lower()!=s[j].lower()):
                return False
            else:
                i=i+1
                j=j-1    
                
        return True

        #   # Remove non-alphanumeric characters and convert to lowercase
        # cleaned = ''.join(char.lower() for char in s if char.isalnum())

        # # Check if the cleaned string is the same forwards and backwards
        # return cleaned == cleaned[::-1]