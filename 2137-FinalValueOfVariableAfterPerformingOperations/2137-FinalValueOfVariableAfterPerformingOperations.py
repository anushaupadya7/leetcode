# Last updated: 21/10/2025, 01:48:51
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val=0
        for op in operations:
            if op == "--X" or op == "X--":
                val-=1
            else:
                val+=1
        return val
