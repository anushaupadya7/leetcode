# Last updated: 19/09/2025, 00:18:54
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # in brute force you initialise count then start traversing from head , n-k times if u traverse from head you will reach node before the node to be deleted

        dummy=ListNode(0,head)
        first=dummy
        second=dummy

        for _ in range(n+1):
            first=first.next

        while first:
            first=first.next
            second=second.next

        second.next=second.next.next

        return dummy.next