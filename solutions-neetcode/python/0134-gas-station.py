class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        total = gas[start] - cost[start]

        while start >= end:
            while total < 0 and start >= end:
                start -= 1
                total += gas[start] - cost[start]
            if start == end:
                return start
            total += gas[end] - cost[end]
            end += 1
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        # This works because the starting_point is positive, which contributes
        # to the answer. If total was positive and became negative at any point,
        # it means that sequence doesn't work. Therefore, a new sequence needs to work
        # because there exists 1 answer. 
        total = 0
        starting_point = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                starting_point = i + 1
        
        return starting_point
        