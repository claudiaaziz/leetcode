class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2



class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n, memo):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            one_step = dfs(n - 1, memo)
            two_steps = dfs(n - 2, memo)

            memo[n] = one_step + two_steps
            return one_step + two_steps
        
        return dfs(n, {})
