# Last updated: 20/09/2025, 22:47:05
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        600
        n=len(nums)

        count0=0
        count1=0
        count2=0

        for i in range(n):
            if nums[i] == 0:
                count0+=1
            if nums[i] == 1:
                count1+=1
            if nums[i] == 2:
                count2+=1
        i=0
        for _ in range(count0):
            nums[i]=0
            i+=1
        for _ in range(count1):
            nums[i]=1
            i+=1
        for _ in range(count2):
            nums[i]=2
            i+=1