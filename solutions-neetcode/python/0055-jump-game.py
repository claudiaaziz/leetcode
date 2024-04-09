class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_idx = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # Starting from the back if the current idx + the current number
            # is greater than the goal, then it's possible to reach the goal.
            # Therefore, you can move the goal to the current index and move backwards.
            if i + nums[i] >= goal_idx:
                goal_idx = i
        
        if goal_idx == 0:
            return True
        else:
            return False

