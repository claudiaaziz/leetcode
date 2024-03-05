class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]





import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #make nums a heap
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        #keep popping until the length of the heap is the same as k.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #add the value to the heap
        heapq.heappush(self.minHeap, val)

        #if the length of the heap is greater than k, pop from it.
        #reason: edge case: the heap's length might've been less than k.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        #since it's a min heap, the first val is the smallest val.
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
