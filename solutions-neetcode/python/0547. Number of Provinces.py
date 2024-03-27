class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        connected_graph = { x: set() for x in range(rows)}

        for row in range(rows):
            for col in range(cols):
                if isConnected[row][col] == 1:
                    connected_graph[row].add(col)
                    connected_graph[col].add(row)
        
        count = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in connected_graph[node]:
                dfs(neighbor)
            
            return True

        for node in connected_graph:
            if dfs(node) == True:
                count+=1
        
        return count
        
                    

        