class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0: return []

        res = []

        sorted_list = sorted(nums)

        count = 0
        result = []
        for num in sorted_list:
            result.append(num)
            count+=1
            if count == 3:
                res.append(result)
                result = []
                count = 0
        
        for sub_list in res:
            if sub_list[-1] - sub_list[0] > k: return []

        return res
            

        