"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary to map old nodes to their corresponding new nodes
        old_to_copy = {None: None}

        # First pass: Create new nodes and build the mapping
        cur = head
        while cur:
            # Create a new node with the same value
            copy = Node(cur.val)
            # Map the old node to the new node
            old_to_copy[cur] = copy
            cur = cur.next

        # Second pass: Connect the new nodes' next and random pointers
        cur = head
        while cur:
            # Get the corresponding new node for the current old node
            copy = old_to_copy[cur]
            # Connect the next pointer
            copy.next = old_to_copy[cur.next]
            # Connect the random pointer
            copy.random = old_to_copy[cur.random]
            cur = cur.next

        # Return the head of the copied linked list, returns the values which are copied
        return old_to_copy[head]
