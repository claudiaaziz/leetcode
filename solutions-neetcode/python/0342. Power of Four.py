class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while i <= n:
            if 4 ** i > n:
                return False
            elif 4 ** i == n:
                return True
            i+=1