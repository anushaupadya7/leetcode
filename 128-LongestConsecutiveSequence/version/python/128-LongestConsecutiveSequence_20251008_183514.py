# Last updated: 08/10/2025, 18:35:14
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length=1
        max_length=1
        number=sorted(set(nums))
        print(number)

        for i in range(len(number)-1):
            if number[i]+1==number[i+1]:
                length+=1
                max_length=max(length,max_length)
            else:
                length=1
        return max_length

            
