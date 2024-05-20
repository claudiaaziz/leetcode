class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]





class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            # If we reach the end of the substring, it means we found a subsequence
            if j == len(t):
                return 1
            # If we didn't reach the end of the substring, but we did reach the end
            # of the main string, it means we didn't find a subsequence
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If there's a match, we can do two things
            if s[i] == t[j]:
                # Increment both i and j, so we include both
                include = dfs(i + 1, j + 1)
                # Increment i but keep j the same, so we're skipping i and hope to
                # find a new match later on
                exclude = dfs(i + 1, j)
                memo[(i, j)] = include + exclude
            else:
                # If it's not a match, we just increment i and keep j the same
                memo[(i, j)] = dfs(i + 1, j)
            
            return memo[(i, j)]
        
        return dfs(0, 0)