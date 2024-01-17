class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum() and s[left].lower() == s[right].lower():
                left+=1
                right-=1
            elif (s[left].isalnum() and not s[right].isalnum()):
                right-=1
            elif (not s[left].isalnum() and s[right].isalnum()):
                left+=1
            elif s[left].isalnum() and s[right].isalnum() and s[left].lower() != s[right].lower():
                return False
            elif (not s[left].isalnum() and not s[right].isalnum()):
                left+=1
                right-=1
        return True
