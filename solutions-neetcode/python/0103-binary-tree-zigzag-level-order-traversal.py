# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        result, zigzagDirection = [], 1
        q = [root]
        while q:
            level, queueLength = [], len(q)
            for i in range(queueLength):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level[::zigzagDirection])
            zigzagDirection *= -1
        return result
    






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #edge case
        if root is None: return []

        #queue to keep track of the nodes
        queue = deque([root])

        #result list to keep track of each level
        res = []

        while queue:
            #sublist to keep track of the values on each level
            sublist = []

            #keep track of the length of the current level
            curr_q_len = len(queue)

            for i in range(curr_q_len):
                popped_ele = queue.popleft()
                sublist.append(popped_ele.val)

                if popped_ele.left:
                    queue.append(popped_ele.left)
                if popped_ele.right:
                    queue.append(popped_ele.right)

            if len(res) % 2 == 0:
                res.append(sublist)
            else:
                res.append(sublist[::-1])

        return res
