# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Define a depth-first search function to calculate the height of the tree
        def dfs(root):
            # If the current node is None, return [True, 0] indicating a balanced tree 
            # and a height of 0
            if not root:
                return [True, 0]

            # Recursively call dfs on the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Check if the current subtree is balanced by ensuring:
            # - The left subtree is balanced (left[0])
            # - The right subtree is balanced (right[0])
            # - The absolute difference in heights of left and right subtrees is at 
            # most 1 (abs(left[1] - right[1]) <= 1)
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

            # Return a list containing the balance status of the current subtree and 
            # determine the maximum height of the left subtree and the maximum height of 
            # the right subtree. 
            return [balanced, max(left[1], right[1]) + 1]

        # Call the dfs function on the root node of the tree and return the balance 
        # status (dfs(root)[0])
        return dfs(root)[0]
