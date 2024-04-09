class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = {}
        res = []
        i, length = 0, len(S)
        for j in range(length):
            c = S[j]
            count[c] = j

        curLen = 0
        goal = 0
        while i < length:
            c = S[i]
            goal = max(goal, count[c])
            curLen += 1

            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res



class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx_dict = {}

        # Get the last index of each char
        for i, char in enumerate(s):
            last_idx_dict[char] = i
        
        # Keep track of the ending idx, size, and res
        end = 0
        size = 0
        res = []
        for i, char in enumerate(s):
            size += 1
            end = max(end, last_idx_dict[char])

            # If i is equal to end, we have reached a partition
            if i == end:
                res.append(size)
                size = 0
        
        return res

        