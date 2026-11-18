from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])
        visited = set()
        # Initialize queue
        queue = deque()
        for row in range(r):
            for col in range(c):
                if grid[row][col] == 0:
                    queue.append((row,col))
                    visited.add((row,col))

        distance = 0
        while queue:
            print(distance)
            qSize = len(queue)
            for i in range(qSize):
                currR, currY = queue.popleft()
                grid[currR][currY] = distance
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    newR,newC = currR+x, currY+y
                    if newR < 0 or newC < 0 or newR >= r or newC >= c or grid[newR][newC] == -1 or grid[newR][newC] != 2147483647 or (newR,newC) in visited:
                        continue
                    visited.add((newR,newC))
                    queue.append((newR,newC))
            distance += 1
        
        