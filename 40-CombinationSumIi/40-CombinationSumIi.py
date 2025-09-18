# Last updated: 19/09/2025, 00:18:45
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        total=0
        candidates.sort()
        def backtrack(start,path,total):
            if total == target:
                result.append(path[:])
                return
            if total>target:
                return

            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,total+candidates[i])
                path.pop()


        backtrack(0,[],0)
        return result