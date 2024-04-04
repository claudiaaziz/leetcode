class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
    



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(amount, memo):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")

            min_change = float("inf")
            for coin in coins:
                min_change = min(min_change, 1 + dfs(amount - coin, memo))
            
            memo[amount] = min_change
            return min_change
        
        answer = dfs(amount, {})
        if answer == float("inf"):
            return -1
        else:
            return answer
        
