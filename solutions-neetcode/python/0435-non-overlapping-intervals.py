class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start
        intervals.sort()
        count = 0

        # Initialize last_end as the first pair's end
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            # If they don't overlap, set the last_end to the current end.
            if start >= last_end:
                last_end = end
            else:
                # If they do overlap, increment count and set the last_end to the
                # shorter end, because we "removed" the longer end.
                count+=1
                last_end = min(last_end, end)

        return count
        