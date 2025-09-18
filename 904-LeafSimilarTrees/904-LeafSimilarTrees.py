# Last updated: 19/09/2025, 00:16:50
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getleaves(root:Optional[TreeNode]) -> int :
            if root == None:
                return []
            
            if root.left == None and root.right== None:
                return [root.val]

            return (getleaves(root.left)+getleaves(root.right))

        return getleaves(root1) == getleaves(root2)