class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output




class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on start
        intervals.sort(key = lambda pair: pair[0])
        # Add the first element to res
        res = [intervals[0]]

        for start, end in intervals:
            last_end = res[-1][1]

            # Needs to be merged and end needs to be updated. Start is always
            # minimized because intervals is sorted. 
            if last_end >= start:
                res[-1][1] = max(last_end, end)
            else:
                # No need to merge
                res.append([start, end])

        return res



        