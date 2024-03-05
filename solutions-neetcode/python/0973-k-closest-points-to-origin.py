class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))
        
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res





import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #create a list to store distance, x, and y
        minHeap = []
        for x, y in points:
            distance = (x**2) + (y**2)
            minHeap.append([distance, x, y])
        
        #turn the list into a heap
        heapq.heapify(minHeap)
        
        #pop from the heap the minimums and append [x, y] to result
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k-=1
        
        #return result
        return res