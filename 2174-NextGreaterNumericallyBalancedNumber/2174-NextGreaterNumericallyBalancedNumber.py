# Last updated: 25/10/2025, 01:35:00
from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def checkbalanced(num : int):
            dict_num=Counter(str(num))
            for digit,count in dict_num.items():
                if int(digit) != count:
                    return False
            return True

        n += 1
        while True:
            if checkbalanced(n):
                return n
            n += 1