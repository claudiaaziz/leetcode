class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]




class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dfs(i, j):
            # Base cases:
            # If i is at the end, return the remaining length of word2
            if i == len(word1):
                return len(word2) - j
            # If j is at the end, return the remaining length of word1
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If there's a match, increment both i and j
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                # When you insert, i stays at the original char, but it takes care of
                # j because we're inserting a match
                insert = dfs(i, j + 1)
                # When we delete, we're removing a char at i, but j stays the same
                delete = dfs(i + 1, j)
                # When we replace, we create a match, so both gets incremented
                replace = dfs(i + 1, j + 1)
                # We get the minimum of the decision tree
                memo[(i, j)] = 1 + min(insert, delete, replace)

            return memo[(i, j)]
        
        return dfs(0, 0)
