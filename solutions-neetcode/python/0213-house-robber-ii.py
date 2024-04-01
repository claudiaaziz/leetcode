class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2





class Solution:
    def rob(self, nums: List[int]) -> int:
        # Trick: Same as Robber 1 except we have to cut off the last element outside
        # of the recursion function.

        def dfs(start, end, memo):
            if (start, end) in memo:
                return memo[(start, end)]
            if start >= end:
                return 0
            
            include = nums[start] + dfs(start + 2, end, memo)
            exclude = dfs(start + 1, end, memo)
            
            memo[(start, end)] = max(include, exclude)
            return max(include, exclude)

        include_start = nums[0] + dfs(2, len(nums) - 1, {})
        exclude_start = dfs(1, len(nums), {})
        return max(include_start, exclude_start)

        

