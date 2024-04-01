class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2




class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i, memo):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0

            include = nums[i] + dfs(i + 2, memo)
            exclude = dfs(i + 1, memo)
            
            memo[i] = max(include, exclude)
            return max(include, exclude)
        
        return dfs(0, {})


        