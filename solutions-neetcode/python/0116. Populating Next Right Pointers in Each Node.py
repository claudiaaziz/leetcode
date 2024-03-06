"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        #since it's a perfect tree, the last node in the current level will point
        #to null
        #we go through the queue, the curr element will point to the next ele,
        #if we're at the end of the sublist, point the curr element to NULL
        queue = deque([root])

        while queue:
            curr_level_len = len(queue)

            for i in range(curr_level_len):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i + 1 == curr_level_len:
                    node.next = None
                else:
                    node.next = queue[0]
        
        return root