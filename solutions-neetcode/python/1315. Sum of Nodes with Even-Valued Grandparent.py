# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = deque([root])
        total = 0
        while queue:
            node = queue.popleft()

            is_even = node.val % 2 == 0

            if node.left:
                queue.append(node.left)
                if is_even:
                    if node.left.left:
                        total+=node.left.left.val
                    if node.left.right:
                        total+=node.left.right.val
            if node.right:
                queue.append(node.right)
                if is_even:
                    if node.right.left:
                        total+=node.right.left.val
                    if node.right.right:
                        total+=node.right.right.val

        return total


        