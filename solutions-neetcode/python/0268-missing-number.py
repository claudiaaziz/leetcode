class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
    


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        #sum range from 0 to length of nums + 1
        for i in range(0, len(nums) + 1):
            total+=i
        #sum nums
        #find difference
        return total - sum(nums)
