# Last updated: 19/09/2025, 00:16:59
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        answer=[0]*n
        stack=[]
        for i,num in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]]<num:
                prev_index=stack.pop()
                answer[prev_index]=i-prev_index

            stack.append(i)
        return answer