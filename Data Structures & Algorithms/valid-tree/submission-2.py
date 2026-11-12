class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        # Valid tree is a graph without cycles
        adj = {i:[] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = set()
        queue = deque([(0,-1)])
        visited.add(0)
        while queue:
            curr, parent = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                queue.append((neighbor,curr))
        return len(visited) == n

