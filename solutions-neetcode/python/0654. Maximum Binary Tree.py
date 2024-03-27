# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        max_val = max(nums)
        max_val_idx = nums.index(max_val)
        left = nums[:max_val_idx]
        right = nums[max_val_idx + 1:]

        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)

        return root
        