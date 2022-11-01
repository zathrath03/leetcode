class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        self.grid = grid
        output = []
        num_cols = len(grid[0])
        for col in range(num_cols):
            output.append(self.find_output(col))
        return output

    def find_output(self, col: int) -> int:
        grid = self.grid
        num_rows = len(grid)
        num_cols = len(grid[0])
        for row in range(num_rows):
            slant = grid[row][col]
            boundary_col = col + slant
            if (0 <= boundary_col < num_cols
                    and grid[row][boundary_col] == slant):
                col += slant
            else:
                return -1
        return boundary_col