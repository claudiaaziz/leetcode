class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res
    

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Keep a window size of each step. If any of the numbers in the window reaches
        # the last index, we're done and can return count.
        left = right = 0
        count = 0

        farthest = 0
        while right < len(nums) - 1:
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            count+=1
        
        return count
            
        
