# Last updated: 19/09/2025, 00:18:25
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTree(node):
            if not node:
                return [None]
            
            return [node.val] + checkTree(node.left) + checkTree(node.right)

        return checkTree(p) == checkTree(q)


        