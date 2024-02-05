class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] % 2 != 0 and nums[right] % 2 == 0:
                # Swap only when left is odd and right is even
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1

            # Move the left pointer if it's at an even number
            if nums[left] % 2 == 0:
                left += 1

            # Move the right pointer if it's at an odd number
            if nums[right] % 2 != 0:
                right -= 1

        return nums
            
            