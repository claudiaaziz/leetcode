class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        i = 0
        while i <= n:
            if 3 ** i > n:
                return False
            elif 3 ** i == n:
                return True
            i+=1
        