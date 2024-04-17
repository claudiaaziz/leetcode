class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1

        # O(E * logV)



from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create a graph with all its neighbors
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v)) # (time, target_node)
        
        # Start the min_heap off with the origin and it takes 0 time. Keep track
        # of a visited set to eliminate duplicates.
        min_heap = [(0, k)]
        min_time = 0
        visited = set()
        # Keep popping min_heap until it's empty because that's when we know
        # we went through every path
        while min_heap:
            # Go down the path with the minimum time. This means we might switch
            # paths throughout the process, but eventually we will always land at
            # the minimum time.
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            
            visited.add(node)
            min_time = time

            for nei_time, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + nei_time, nei))
        
        # Check if all nodes have been visited
        return min_time if len(visited) == n else -1
        

        