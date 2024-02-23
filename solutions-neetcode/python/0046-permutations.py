class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []

        def dfs(current_permutation, remaining_numbers):
            if remaining_numbers == []:
                combinations.append(current_permutation.copy())
                return
            
            for i in range(len(remaining_numbers)):
                current_permutation.append(remaining_numbers[i])

                dfs(current_permutation, remaining_numbers[0:i] + remaining_numbers[i+1:])

                current_permutation.pop()
        
        dfs([], nums)

        return combinations