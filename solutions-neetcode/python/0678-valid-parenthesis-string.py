# Dynamic Programming: O(n^2)
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {(len(s), 0): True}  # key=(i, leftCount) -> isValid

        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]

            if s[i] == "(":
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ")":
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                dp[(i, left)] = (
                    dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left)
                )
            return dp[(i, left)]

        return dfs(0, 0)


# Greedy: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:  # required because -> s = ( * ) (
                leftMin = 0
        return leftMin == 0





class Solution:
    def checkValidString(self, s: str) -> bool:
        start_paren = []
        star_paren = []

        for i, char in enumerate(s):
            if char == "(":
                start_paren.append(i)
            elif char == "*":
                star_paren.append(i)
            else:
                if start_paren:
                    start_paren.pop()
                elif star_paren:
                    star_paren.pop()
                else:
                    return False
            
        while start_paren and star_paren:
            if start_paren[-1] > star_paren[-1]:
                return False
            
            start_paren.pop()
            star_paren.pop()
        
        if start_paren:
            return False
        else:
            return True

                
        