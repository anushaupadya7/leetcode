# Last updated: 19/09/2025, 00:18:10
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        curr=slow.next
        slow.next=None

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        first=head
        second=prev

        while second:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2

        


        