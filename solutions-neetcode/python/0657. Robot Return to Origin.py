class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves_dict = {
            "R": [1, 0],
            "L": [-1, 0],
            "U": [0, 1],
            "D": [0, -1]
        }

        start = [0, 0]
        for move in moves:
            start[0] += moves_dict[move][0]
            start[1] += moves_dict[move][1]
        
        return start == [0, 0]

        