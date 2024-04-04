class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Set everything to be the first element
        global_max = curr_max = curr_min = nums[0]

        # Go through the rest of the numbers
        for i in range(1, len(nums)):
            # If the number you encounter is negative, swap curr_max and curr_min
            # because multiplying them will have opposite results
            if nums[i] < 0:
                curr_max, curr_min = curr_min, curr_max

            # Because it is a subarray, either continue the subarray or cut it off
            # and start a new subarray. Ex: [-1, 8]
            curr_max = max(nums[i], curr_max * nums[i])
            curr_min = min(nums[i], curr_min * nums[i])

            # Set global_max
            global_max = max(global_max, curr_max)
        
        return global_max

        