class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res






class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #sort the list so we can see back to back numbers
        candidates.sort()
        res = []

        #helper function that takes in the current list, the current index, and the total
        def dfs(sublist, i, total):
            #base case 1: we found a combination that sums to the target
            if total == target:
                res.append(sublist.copy())
                return
            
            #base case 2: combination is too big or we went through the entire candidates
            #list
            if total > target or i >= len(candidates):
                return
            
            #choice 1: include the current candidate
            sublist.append(candidates[i])
            #we move onto the next candidate and update total
            dfs(sublist, i+1, total + candidates[i])

            #choice 2: we don't include current candidate
            sublist.pop()
            #we remove all repeats
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            #we move onto a new candidate and total remains the same
            dfs(sublist, i+1, total)

        #start off with an empty sublist, index 0, 0 total
        dfs([], 0, 0)
        
        return res
        