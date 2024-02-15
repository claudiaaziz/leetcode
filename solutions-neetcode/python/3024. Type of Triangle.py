class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        n = len(set(nums))
        if n == 1:
            return "equilateral"
        elif n == 2:
            return "isosceles"
        else:
            return "scalene"