class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        if k > num_rows + num_cols - 3:
            return num_rows + num_cols - 2

        target = (num_rows - 1, num_cols - 1)
        state = (0, 0, k)

        visited: set[tuple[int, int, int]] = set()
        visited.add(state)

        queue: deque[tuple[int, tuple[int, int, int]]] = deque()
        queue.append((0, state))

        while queue:
            steps, (row, col, remaining) = queue.popleft()

            if (row, col) == target:
                return steps

            for row, col in [(row + 1, col), (row, col + 1),
                             (row - 1, col), (row, col - 1)]:
                if (0 <= row < num_rows) and (0 <= col < num_cols):
                    new_remaining = remaining - grid[row][col]
                    state = (row, col, new_remaining)

                    if remaining >= 0 and state not in visited:
                        queue.append((steps + 1, state))
                        visited.add(state)

        return -1