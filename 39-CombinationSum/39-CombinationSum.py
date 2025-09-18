# Last updated: 19/09/2025, 00:18:46
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        total=0
        def backtrack(start,path,total):
            if total == target:
                result.append(path[:])
                return
            if total>target:
                return

            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,total+candidates[i])
                path.pop()


        backtrack(0,[],0)
        return result