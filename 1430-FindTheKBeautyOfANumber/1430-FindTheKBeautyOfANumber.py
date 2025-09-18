# Last updated: 19/09/2025, 00:16:39
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str=str(num)
        count=0
        n=len(num_str)

        for i in range(n-k+1):
            sub_num=int(num_str[i:i+k])
            if sub_num!=0 and num % sub_num==0:
                count+=1
        return count