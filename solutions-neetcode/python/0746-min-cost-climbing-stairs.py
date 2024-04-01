class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])




class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last_idx = len(cost)

        def dfs(i, memo):
            if i in memo:
                return memo[i]
            if i >= last_idx:
                return 0
            
            one_step = cost[i] + dfs(i + 1, memo)
            two_steps = cost[i] + dfs(i + 2, memo)

            memo[i] = min(one_step, two_steps)
            return min(one_step, two_steps)
        
        return min(dfs(0, {}), dfs(1, {}))


        