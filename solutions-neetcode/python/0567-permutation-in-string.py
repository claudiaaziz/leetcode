class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    

    
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_length = len(s1)
        s1_chars = Counter(s1)
        s2_chars = Counter(s2[:window_length])

        if window_length > len(s2): return False
        
        if s1_chars == s2_chars: return True
        
        for i in range(window_length, len(s2)):
            s2_chars[s2[i - window_length]]-=1

            if s2[i] in s2_chars:
                s2_chars[s2[i]]+=1
            else:
                s2_chars[s2[i]] = 1
            
            if s1_chars == s2_chars: return True 

        return False
