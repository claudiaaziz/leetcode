class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"




class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        no_flip = set()

        # Capture all the O's that shouldn't be flipped to X's
        def dfs(row, col):
            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return
            if (row, col) in no_flip:
                return
            if board[row][col] == "X":
                return
            
            no_flip.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Only do the edges
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)
        
        # If the position is an "O" and it's not in no_flip, it means it can be flipped
        # into an "X".
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in no_flip:
                    board[row][col] = "X"
        





        