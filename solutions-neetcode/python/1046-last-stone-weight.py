class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

# There's a private _heapify_max method.
# https://github.com/python/cpython/blob/1170d5a292b46f754cd29c245a040f1602f70301/Lib/heapq.py#L198
class Solution(object):
    def lastStoneWeight(self, stones):
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)
        
        stones.append(0)
        return stones[0]






class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #make them all negative because we are trying to do max heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        #keep going until there's 1 or no stones left
        while len(stones) > 1:
            #get the first two, make them positive
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            #if the second one is smaller, find the negative difference
            #and add it to the heap
            if second < first: heapq.heappush(stones, second - first)
        
        #add 0 at the end and return the first element
        stones.append(0)
        return abs(stones[0])
