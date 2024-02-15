class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiopQWERTYUIOP')
        row2 = set('asdfghjklASDFGHJKL')
        row3 = set('zxcvbnmZXCVBNM')
        ans = []

        for word in words:
            rows_used = set()
            for letter in word:
                if letter in row1:
                    rows_used.add(1)
                elif letter in row2:
                    rows_used.add(2)
                else:
                    rows_used.add(3)
            if len(rows_used) == 1:
                ans.append(word)

        return ans