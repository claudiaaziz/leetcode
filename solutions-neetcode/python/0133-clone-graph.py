class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
    






from collections import deque
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}  # Dictionary to store the mapping of original nodes to their clones
        queue = deque([node])  # Queue for BFS traversal

        clone = Node(node.val)  # Create a clone of the input node
        visited[node] = clone  # Add the original node and its clone to the visited dictionary
        
        while queue:
            current = queue.popleft()  # Pop a node from the queue
            
            for neighbor in current.neighbors:  # Iterate through the neighbors of the current node
                if neighbor not in visited:  # If the neighbor hasn't been visited before
                    neighbor_clone = Node(neighbor.val)  # Create a clone of the neighbor
                    visited[neighbor] = neighbor_clone  # Add the original neighbor and its clone to the visited dictionary
                    queue.append(neighbor)  # Add the neighbor to the queue for further exploration
                visited[current].neighbors.append(visited[neighbor])  # Update the neighbor list of the current clone node
        
        return clone  # Return the clone of the input node
