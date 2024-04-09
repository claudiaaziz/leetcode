class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3



class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good_set = set()

        for sublist in triplets:
            # If any of the numbers in the sublist is greater than target, we can skip
            # that sublist because max will be bigger than target.
            if sublist[0] > target[0] or sublist[1] > target[1] or sublist[2] > target[2]:
                continue
            
            # if a number in a good sublist is equal to a number in the target,
            # add the index to the set because it works. 
            for i, num in enumerate(sublist):
                if sublist[i] == target[i]:
                    good_set.add(i)
        
        # The set should be 3 numbers(0, 1, 2)
        return len(good_set) == 3


        