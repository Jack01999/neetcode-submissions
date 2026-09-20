class Solution:
    def floodFill(self, grid, x, y, newVal):
        if (x<0 or x>=len(grid)) or (y<0 or y>=len(grid[0])) or grid[x][y] != "1":
            return
        grid[x][y] = newVal

        self.floodFill(grid, x+1, y, newVal)
        self.floodFill(grid, x, y+1, newVal)
        self.floodFill(grid, x-1, y, newVal)
        self.floodFill(grid, x, y-1, newVal)
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    res += 1
                    self.floodFill(grid, x, y, "0")
        return res
        