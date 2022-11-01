class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        output = []
        num_rows, num_cols = len(grid), len(grid[0])
        # perform a dfs for each column in the grid
        for col in range(num_cols):
            for row in range(num_rows):
                slant = grid[row][col]
                boundary_col = col + slant

                # Check if stuck in current cell
                # - if current cell is 1, check if next cell is -1 or boundary
                # - if current cell is -1, check if prev cell is -1 or boundary
                # - can add value of current cell to current column instead
                #   of using two cases
                if (boundary_col < 0 or boundary_col >= num_cols
                        or grid[row][boundary_col] == -slant):
                    output.append(-1)
                    break
                elif row == num_rows - 1:
                    output.append(col + slant)
                    break
                else:
                    col += slant
        # Keep track of cells that will trap balls so we don't need to check?
        return output