class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        
        frequencies = {}
        for num, freq in counts.items():
            if freq not in frequencies:
                frequencies[freq] = [num]
            else:
                frequencies[freq].append(num)

        sorted_keys = sorted(frequencies.keys())

        ans = []
        for key in sorted_keys:
            values = frequencies[key]
            values.sort(reverse=True)
            for value in values:
                ans.extend([value] * key)
        return ans