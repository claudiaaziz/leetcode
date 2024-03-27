# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, currentPath):
            currentPath.append(str(node.val))
            if node.left is None and node.right is None:
                ans.append('->'.join(currentPath))
                return
            if node.left:
                dfs(node.left, currentPath)
                currentPath.pop()
            if node.right:
                dfs(node.right, currentPath)
                currentPath.pop()

        dfs(root, [])
        return ans
            

        