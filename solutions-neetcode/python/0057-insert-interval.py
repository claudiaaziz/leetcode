class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # 3 conditions to consider:

        # 1. Intervals that come strictly before the newInterval
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

        # 2. Intervals that merge with the newInterval
        for j in range(len(intervals)):
            if intervals[j][0] <= newInterval[1] and newInterval[0] <= intervals[j][1]:
                newInterval[0] = min(intervals[j][0], newInterval[0])
                newInterval[1] = max(intervals[j][1], newInterval[1])
        res.append(newInterval)
        
        # 3. Intervals that come strictly after the newInterval
        for k in range(len(intervals)):
            if intervals[k][0] > newInterval[1]:
                res.append(intervals[k])
    
        return res



                
        