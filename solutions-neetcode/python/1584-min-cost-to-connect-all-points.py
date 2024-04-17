class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res





class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create a graph where the key is a node and the values are its neighbors
        # that includes the [cost, node]
        graph = { i:[] for i in range(len(points)) }
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        # Initialize a cost and go through the graph until we visit every node by
        # having a visited set
        cost = 0
        visited = set()
        min_heap = [[0, 0]] # [cost, node]
        
        while len(visited) < len(points):
            min_cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            cost += min_cost
            visited.add(node)

            for nei_cost, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, [nei_cost, nei])
        
        print(graph)
        return cost
        