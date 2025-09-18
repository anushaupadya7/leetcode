# Last updated: 19/09/2025, 00:17:38
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        answer=[1]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]

        print(prefix)

        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]

        print(suffix)

        for i in range(n):
            answer[i]=prefix[i]*suffix[i]
        return answer
        

