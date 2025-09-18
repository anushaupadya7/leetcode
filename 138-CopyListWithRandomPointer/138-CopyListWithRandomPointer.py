# Last updated: 19/09/2025, 00:18:12
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            new_node = Node(current.val, current.next, None)
            current.next = new_node
            current = new_node.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        current = head
        copied_head = head.next
        copied_current = copied_head

        while current:
            current.next = current.next.next
            copied_current.next = copied_current.next.next if copied_current.next else None
            current = current.next
            copied_current = copied_current.next

        return copied_head