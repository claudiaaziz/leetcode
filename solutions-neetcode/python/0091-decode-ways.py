class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]






class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i, memo):
            if i in memo:
                return memo[i]
            # Base case: if index reaches the end of string, return 1
            if i == len(s):
                return 1
            
            count = 0

            # Case 1: Single-digit decoding
            if s[i] != "0":
                count += dfs(i + 1, memo)
            
            # Case 2: Two-digit decoding
            if i + 1 < len(s) and (s[i] == "1" or 
                (s[i] == "2" and s[i + 1] in "0123456")):
                count += dfs(i + 2, memo)
            
            memo[i] = count
            return count
        
        return dfs(0, {})
            


            



            

        