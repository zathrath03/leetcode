class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        self.grid = grid
        output = []
        num_cols = len(grid[0])
        for col in range(num_cols):
            output.append(self.find_output(col))
        return output

    def find_output(self, col: int) -> int:
        num_rows = len(self.grid)
        for row in range(num_rows):
            if (self.is_trapped(row, col)):
                return -1
            col += self.grid[row][col]
        return col

    def is_trapped(self, row, col):
        slant = self.grid[row][col]
        boundary_col = col + slant
        num_cols = len(self.grid[0])
        return (boundary_col < 0 or boundary_col >= num_cols
                or self.grid[row][boundary_col] != slant)
