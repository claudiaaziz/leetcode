class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # O(n * m) O(n)



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        def dfs(r, c, memo):
            if (r, c) in memo:
                return memo[(r, c)]
            if r == rows - 1 and c == cols - 1:
                return 1
            if r >= rows or c >= cols:
                return 0
            
            row_pos = dfs(r + 1, c, memo)
            col_pos = dfs(r, c + 1, memo)

            memo[(r, c)] = row_pos + col_pos
            return row_pos + col_pos
        
        return dfs(0, 0, {})
        