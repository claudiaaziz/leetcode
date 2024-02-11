# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        #returns the height for the current node
        def height(root):
            nonlocal diameter
            
            if not root:
                return 0
            
            #returns the max height on the left side
            left = height(root.left)
            #returns the max height on the right side
            right = height(root.right)

            #updates the max diameter by adding both sides
            diameter = max(diameter, left + right)

            curr_height = max(left, right) + 1

            return curr_height
        
        height(root)

        return diameter

