class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
    




class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #sort to make sure we can track back to back numbers
        nums.sort()

        #result array
        res = []

        #helper takes in the current subset and an index to find the current number
        def dfs(subset, i):
            #if the index is out of bounds, we have a completed subset
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #include same numbers
            subset.append(nums[i])
            dfs(subset, i+1)

            #not include same numbers
            subset.pop()
            #keep increasing i until there isn't back to back numbers
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(subset, i+1)
        
        #start recursion
        dfs([], 0)

        #return completed subsets
        return res

