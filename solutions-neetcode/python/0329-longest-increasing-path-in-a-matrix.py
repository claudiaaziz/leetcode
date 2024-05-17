class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())






class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Get the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Memoize to make it more efficient
        memo = {}

        # Helper to calculate longest path
        def dfs(r, c, prev_val):
            # Return 0 if any of these are true
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                matrix[r][c] <= prev_val):
                return 0
            # Return the memo if it's in there
            if (r, c) in memo:
                return memo[(r, c)]
            
            # Get the max of the four paths
            count = 1
            count = max(count, 
                1 + dfs(r + 1, c, matrix[r][c]), 
                1 + dfs(r - 1, c, matrix[r][c]), 
                1 + dfs(r, c + 1, matrix[r][c]), 
                1 + dfs(r, c - 1, matrix[r][c]))
            memo[(r, c)] = count

            # Return the max at that position
            return count
            
        for row in range(rows):
            for col in range(cols):
                # Go through every position, some are fast because it got memoized
                dfs(row, col, -1)
        
        # Return the max of the memoized values
        return max(memo.values())
        