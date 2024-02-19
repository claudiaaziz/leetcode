class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #2 pointers, pointer1 would be at 0, pointer2 would be at 1
        pointer_even = 0
        pointer_odd = 1

        while pointer_even < len(nums) and pointer_odd < len(nums):
            if nums[pointer_even] % 2 == 0:
                pointer_even+=2
                if pointer_even >= len(nums):
                    break
            if nums[pointer_odd] % 2 != 0:
                pointer_odd+=2
                if pointer_odd >= len(nums):
                    break
            
            if nums[pointer_even] % 2 != 0 and nums[pointer_odd] % 2 == 0:
                nums[pointer_even], nums[pointer_odd] = nums[pointer_odd], nums[pointer_even]
        
        return nums
        