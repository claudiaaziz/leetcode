class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_s = 0
        left = 0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]] = 1
            
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]]-=1
                left+=1
            
            max_s = max(max_s, right - left + 1)

        return max_s