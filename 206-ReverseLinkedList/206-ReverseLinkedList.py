# Last updated: 03/10/2025, 00:24:44
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        
        return prev