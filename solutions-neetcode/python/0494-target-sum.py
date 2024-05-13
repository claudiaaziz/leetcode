class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)




class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, amt):
            if (i, amt) in memo:
                return memo[(i, amt)]
            if i == len(nums) and amt == target:
                return 1
            if i == len(nums) and (amt > target or amt < target):
                return 0
            
            plus = dfs(i + 1, amt + nums[i])
            minus = dfs(i + 1, amt - nums[i])

            memo[(i, amt)] = plus + minus
            return plus + minus
        
        return dfs(0, 0)
        