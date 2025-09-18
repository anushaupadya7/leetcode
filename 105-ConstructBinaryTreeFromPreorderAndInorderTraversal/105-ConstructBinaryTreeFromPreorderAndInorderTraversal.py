# Last updated: 19/09/2025, 00:18:22
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map={val:index for index,val in enumerate(inorder)}
        def build(pre_start,pre_end,in_start,in_end):
            if pre_start>pre_end or in_start>in_end:
                return None

            root_val=preorder[pre_start]
            root=TreeNode(root_val)
            
            root_indx=index_map[root_val]
            left_tree_size=root_indx-in_start

            root.left=build(pre_start+1,pre_start+left_tree_size,in_start,root_indx-1)
            root.right=build(pre_start+left_tree_size+1,pre_end,root_indx+1,in_end)
            return root

        return build(0,len(preorder)-1,0,len(inorder)-1)