class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")

        for i in range(len(arr) - 1):
            j = i + 1
            difference = abs(arr[j] - arr[i])
            min_diff = min(min_diff, difference)
        
        res = []
        for i in range(len(arr) - 1):
            j = i + 1
            if abs(arr[j] - arr[i]) == min_diff:
                res.append([arr[i], arr[j]])
                
        return res
