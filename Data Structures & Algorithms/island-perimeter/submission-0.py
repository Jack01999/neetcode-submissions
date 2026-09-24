class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    if x-1 < 0:
                        res += 1
                    if x+1 >= len(grid):
                        res += 1
                    if y-1 < 0:
                        res += 1
                    if y+1 >= len(grid[x]):
                        res += 1
                    
                    if x-1 >= 0 and grid[x-1][y] == 0:
                        res += 1
                    if x+1 < len(grid) and grid[x+1][y] == 0:
                        res += 1
                    if y-1 >= 0 and grid[x][y-1] == 0:
                        res += 1
                    if y+1 < len(grid[x]) and grid[x][y+1] == 0:
                        res += 1

        return res
        