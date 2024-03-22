class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1





from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Keep track of how many fresh oranges there are and the positions of
        # the rotten oranges.
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh+=1
                if grid[row][col] == 2:
                    queue.append([row, col])
        
        # Go through the queue and turn fresh oranges into rotten oranges.
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            queue_len = len(queue)
            for i in range(queue_len):
                r, c = queue.popleft()
                for d1, d2 in directions:
                    nr, nc = r + d1, c + d2
                    if (nr < 0 or nr >= rows) or (nc < 0 or nc >= cols) or grid[nr][nc] != 1:
                        continue
                    # Once a fresh orange becomes a rotten orange, add the new rotten
                    # orange to the queue and decrement fresh.
                    grid[nr][nc] = 2
                    queue.append([nr, nc])
                    fresh -= 1
            # Once a whole cycle of a queue completes, time increments by 1.
            time += 1

        # Return the time if there are no fresh oranges, else return -1.
        if fresh == 0:
            return time
        else:
            return -1


        

        