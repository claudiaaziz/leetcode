class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res



class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # Odd 
            left = i
            right = i
            count += self.helper(left, right, s)
            
            # Even
            left = i
            right = i + 1
            count += self.helper(left, right, s)

        return count
    
    def helper(self, pt1, pt2, string):
        res = 0

        while pt1 >= 0 and pt2 < len(string) and string[pt1] == string[pt2]:
            res += 1
            pt1 -= 1
            pt2 += 1
        
        return res



        
