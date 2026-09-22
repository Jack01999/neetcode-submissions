class Solution:
    

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def floodIsland(x, y):
            if (x<0 or x>=rows) or (y<0 or y>=cols) or grid[x][y] == 0:
                return 0

            grid[x][y] = 0
            return (1 + floodIsland(x+1, y) + floodIsland(x-1, y) + floodIsland(x, y+1) + floodIsland(x, y-1))
        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                val = floodIsland(x, y)
                res = max(res, val)
        return res
        