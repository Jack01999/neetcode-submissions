from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adj list
        adj = {i:[] for i in range(numCourses)}
        indegrees = {i:0 for i in range(numCourses)}
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegrees[prereq[0]] += 1

        queue = deque([i for i in indegrees if indegrees[i] == 0])
        nodeVisited = 0
        while queue:
            curr = queue.popleft()
            nodeVisited += 1
            for neighbor in adj[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        # If every value in indegrees is 0, then it's valid
        return nodeVisited == numCourses