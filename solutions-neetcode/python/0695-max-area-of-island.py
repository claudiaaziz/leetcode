class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
    



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def explore(grid, row, col):
            if row < 0 or row >= rows:
                return 0
            if col < 0 or col >= cols:
                return 0
            if grid[row][col] == 0:
                return 0
            if (row, col) in visited:
                return 0
            
            visited.add((row, col))
            count = 1

            count += explore(grid, row + 1, col)
            count += explore(grid, row - 1, col)
            count += explore(grid, row, col + 1)
            count += explore(grid, row, col - 1)

            return count

        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, explore(grid, row, col))
        
        return max_area
        
