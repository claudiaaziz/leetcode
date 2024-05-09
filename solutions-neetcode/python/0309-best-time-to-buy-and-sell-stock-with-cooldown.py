class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)





class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dfs(i, buying):
            # Base case if index is out of bounds
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            # If buying is true
            if buying:
                # Buy the stock and set buying to false
                buy = dfs(i + 1, not buying) - prices[i]
                # Don't buy the stock and keep buying as true
                cooldown = dfs(i + 1, buying)
                # Return the max of the 2 decisions
                memo[(i, buying)] = max(buy, cooldown)
            # If buying is false
            else:
                # Sell the stock and set buying to true. If you choose to sell,
                # there's a 1 day cooling period, which is why it's i + 2
                sell = dfs(i + 2, not buying) + prices[i]
                # Don't see the stock and keep buying as false
                cooldown = dfs(i + 1, buying)
                # Return the max of the 2 decisions
                memo[(i, buying)] = max(sell, cooldown)
        
            return memo[(i, buying)]

        # Start at first price and set buying to true. From there, we can choose
        # to buy or not buy
        return dfs(0, True)