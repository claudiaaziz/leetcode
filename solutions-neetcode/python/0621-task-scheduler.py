class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


# Greedy algorithm
class Solution(object):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_count = max(counter.values())
        min_time = (max_count - 1) * (n + 1) + \
                    sum(map(lambda count: count == max_count, counter.values()))
    
        return max(min_time, len(tasks))
    






from collections import Counter
import heapq
from collections import deque 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Turn tasks into a dictionary
        count = Counter(tasks)

        # Turn values into a max_heap by making the max values negative
        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)

        # Make a queue to keep track of the [freq, idle_time]
        queue = deque()
        time = 0

        # If there are still tasks or we need to wait for the queue, keep going
        while max_heap or queue:
            # Each time this loop runs, increase the time
            time+=1

            # If there are still tasks
            if max_heap:
                # Make freq increase so it's closer to 0 and pop it from the heap
                freq = 1 + heapq.heappop(max_heap)
                
                # If the freq isn't 0, it needs to be queued until it's 0.
                if freq < 0:
                    queue.append([freq, time + n])
            
            # If the idle_time == time, we can start another task
            if queue and queue[0][1] == time:
                # Take the freq and add it to the heap to repeat the process
                next_ele_freq = queue.popleft()[0]
                heapq.heappush(max_heap, next_ele_freq)
        
        # Return the time at the end
        return time