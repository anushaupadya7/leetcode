# Last updated: 19/09/2025, 00:16:26
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        while slow: 
            next_node=slow.next
            slow.next=prev
            prev=slow
            slow=next_node

        first,second=head,prev
        max_sum=0

        while second:
            max_sum=max(max_sum,first.val+second.val)
            first=first.next
            second=second.next
        return max_sum



        