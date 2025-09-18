# Last updated: 19/09/2025, 00:18:00
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # store={}
        # for i,num in enumerate(numbers):
        #     complement=target-num
        #     if complement in store:
        #         return [store[complement]+1,i+1]
        #     store[num]=i
        # return []

        left,right=0,len(numbers)-1
        while(left<right):
            current_sum=numbers[left]+numbers[right]
            if current_sum==target:
                return [left+1,right+1]
            elif current_sum<target:
                left+=1
            else:
                right-=1