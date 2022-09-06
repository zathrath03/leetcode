class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0        
        
                        
        def sinkIsland(r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                if r > 0:
                    sinkIsland(r-1, c)
                if r < R:
                    sinkIsland(r+1, c)
                if c > 0:
                    sinkIsland(r, c-1)
                if c < C:
                    sinkIsland(r, c+1)


        R = len(grid) - 1
        C = len(grid[0]) - 1
        numIslands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    sinkIsland(r, c)
                    numIslands += 1

        return numIslands