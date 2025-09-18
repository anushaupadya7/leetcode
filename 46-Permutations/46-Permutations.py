# Last updated: 19/09/2025, 00:18:42
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result=[]
        
        # def backtrack(path,used):
        #     if len(nums)==len(path):
        #         result.append(path[:])
        #         return
        #     for i in range(len(nums)):
        #         if not used[i]:
        #             used[i]=True
        #             path.append(nums[i])
        #             backtrack(path,used)
        #             path.pop()
        #             used[i]=False

        # backtrack([],[False]*len(nums))
        # return result
        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start] 
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  

        backtrack(0)
        return result