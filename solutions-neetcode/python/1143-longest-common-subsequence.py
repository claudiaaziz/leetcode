class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]




class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dfs(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If i or j is at the end of the string, return 0
            if i == len(text1) or j == len(text2):
                return 0
            
            # If the letters are the same, increase answer by 1 and keep going
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1, memo)
                return memo[(i, j)]
            else:
                # If the letters are not the same, get the max of two strings,
                # where i increased by 1 or j increased by 1
                memo[(i, j)] = max(dfs(i + 1, j, memo), dfs(i, j + 1, memo))
                return memo[(i, j)]
        
        return dfs(0, 0, {})
