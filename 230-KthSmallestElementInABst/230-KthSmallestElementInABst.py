# Last updated: 19/09/2025, 00:17:41
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def inorder(node):
        #     if not node:
        #         return []
        #     return inorder(node.left)+[node.val]+inorder(node.right)
        # return inorder(root)[k-1]

        stack=[]
        count=0
        current=root

        while current or stack:
            while current:
                stack.append(current)
                current=current.left
        
            current=stack.pop()
            count+=1

            if count==k:
                return current.val
            
            current=current.right
        
        
 
                
         
          
               
            