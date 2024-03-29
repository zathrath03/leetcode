# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    MAX_MATRIX_LENGTH = 100

    def leftMostColumnWithOne(self, binaryMatrix) -> int:

        self.binaryMatrix = binaryMatrix
        self.rows, self.cols = binaryMatrix.dimensions()
        self.leftmost_column_with_one = self.MAX_MATRIX_LENGTH + 1

        rows_with_ones = self.get_rows_with_ones()

        for row in rows_with_ones:
            self.binary_search_row(row)

        return (
            self.leftmost_column_with_one
            if self.leftmost_column_with_one <= self.MAX_MATRIX_LENGTH
            else -1
        )

    def binary_search_row(self, row: int) -> None:
        left, right = 0, min(self.leftmost_column_with_one, self.cols - 1)
        if self.binaryMatrix.get(row, right) == 0:
            return

        while left <= right:
            mid = (left + right) // 2
            if self.binaryMatrix.get(row, mid) == 1:
                self.leftmost_column_with_one = min(
                    self.leftmost_column_with_one, mid
                )
                right = mid - 1
            else:
                left = mid + 1
                if left >= self.leftmost_column_with_one:
                    break

    def get_rows_with_ones(self) -> set:
        rows_with_ones = set()
        for row in range(self.rows):
            if self.binaryMatrix.get(row, self.cols - 1) == 1:
                rows_with_ones.add(row)
        return rows_with_ones
