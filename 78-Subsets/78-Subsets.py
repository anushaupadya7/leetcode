# Last updated: 19/09/2025, 00:18:30
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result=[[]]

        # for num in nums:
        #     result=result+[curr+[num] for curr in result]

        # return result
        n = len(nums)
        result = []

        for i in range(2 ** n):  # i goes from 0 to 7
            subset = []
            for j in range(n):  # check each bit position
                if i & (1 << j):  # if j-th bit is set in i
                    subset.append(nums[j])
            result.append(subset)
        
        return result