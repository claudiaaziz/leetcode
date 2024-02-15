# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Define a recursive function to count the number of good nodes
        def dfs(node, max_value):
            # Base case: If the node is None, return 0
            if node is None: 
                return 0

            res = 0  # Initialize the result variable to count good nodes
            # Check if the value of the current node is greater than or equal to max_value
            if node.val >= max_value: 
                res += 1  # Increment the count of good nodes
                max_value = max(max_value, node.val)  # Update max_value to the maximum value seen so far

            # Recursively count the number of good nodes in the left and right subtrees
            res += dfs(node.left, max_value)
            res += dfs(node.right, max_value)

            return res  # Return the total count of good nodes
        
        # Call the recursive function with the root of the binary tree and the initial max_value as the value of the root
        return dfs(root, root.val)
