class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res




class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            # If the current sum is negative, we can reset it because it will
            # cause us to get a smaller number.
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
        
