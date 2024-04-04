class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]




class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for faster lookup
        word_set = set(wordDict)
        
        # Recursive function to check if string can be segmented
        def subWord(word, memo):
            if word in memo:
                return memo[word]
            # Base case: if string is empty, return True
            if len(word) == 0:
                return True
            
            # Iterate through all possible substrings
            for i in range(1, len(word) + 1):
                # Check if substring from 0 to i exists in wordDict
                if word[:i] in word_set:
                    # Recursively check the remaining substring
                    if subWord(word[i:], memo):
                        memo[word] = True
                        return True
            # No segmentation possible
            memo[word] = False
            return False
        
        # Start recursive function from the beginning of the string
        return subWord(s, {})


        