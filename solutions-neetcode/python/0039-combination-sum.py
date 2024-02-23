class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
    



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #where all the combinations will go
        res = []

        #recursive function: takes in index, combination, total so far
        def dfs(i, sublist, total):
            #base case 1: we found a combination that sums to the target
            if total == target:
                res.append(sublist.copy())
                return
            
            #base case 2: combination is too big or we went through the entire candidates
            #list
            if total > target or i >= len(candidates):
                return
            
            #choice 1: include the current candidate, repeats allowed
            sublist.append(candidates[i])
            #we stay at the current candidate and we need to update total
            dfs(i, sublist, total + candidates[i])

            #choice 2: we don't include current candidate
            sublist.pop()
            #we move onto a new candidate and total remains the same
            dfs(i + 1, sublist, total)
        
        #start off at index 0, empty sublist, 0 total
        dfs(0, [], 0)

        return res
