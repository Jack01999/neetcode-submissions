from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adj list
        adj = {i:[] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        res = 0

        for i in range(n):
            if i in visited:
                continue
            else:
                res += 1
                queue = deque([i])
                visited.add(i)
                while queue:
                    curr = queue.popleft()
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return res

        