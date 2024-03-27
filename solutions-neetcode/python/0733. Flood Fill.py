from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_pos = [sr, sc]
        start_color = image[sr][sc]
        if start_color == color:
            return image

        queue = deque([start_pos])
        directions = [1, 0], [-1, 0], [0, 1], [0, -1]
        while queue:
            row, col = queue.popleft()
            for r, c in directions:
                if 0 <= row + r < len(image) and 0 <= col + c  < len(image[0]) and image[row + r][col + c ] == start_color:
                    image[row + r][col + c] = color
                    queue.append([row + r, col + c])
            image[row][col] = color
        
        return image


