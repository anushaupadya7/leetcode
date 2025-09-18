# Last updated: 19/09/2025, 00:16:35
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_value):
            if not node:
                return 0
            
            good = 1 if node.val >= max_value else 0 
            max_value = max(max_value,node.val)

            good=good+dfs(node.left,max_value)
            good=good+dfs(node.right,max_value)

            return good
        return dfs(root,root.val)