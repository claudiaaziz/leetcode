class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #convert nums to a set
        nums_set = set(nums)
        nums_list = list(nums_set)
        nums_list.sort(reverse=True)

        #if the length is equal or greater than 3, return index 2's element
        #else return the max
        if len(nums_list) >= 3:
            return nums_list[2]
        else:
            return nums_list[0]