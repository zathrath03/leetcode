# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    MAX_MATRIX_LENGTH = 100
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        self.binaryMatrix = binaryMatrix
        rows, cols = binaryMatrix.dimensions()
        last_column_index = cols - 1
        rows_with_ones = set()
        leftmost_column_with_one = self.MAX_MATRIX_LENGTH + 1
        
        for row in range(rows):
            if binaryMatrix.get(row, last_column_index) == 1:
                rows_with_ones.add(row)
                leftmost_column_with_one = last_column_index
        
        for row in rows_with_ones:
            this_row_leftmost_column_with_one = self.binary_search_row(row)
            leftmost_column_with_one = min(leftmost_column_with_one, this_row_leftmost_column_with_one)
                
        return leftmost_column_with_one if leftmost_column_with_one <= self.MAX_MATRIX_LENGTH else -1
    
    def binary_search_row(self, row: int) -> int:
        _, cols = self.binaryMatrix.dimensions()
        leftmost_column_with_one = self.MAX_MATRIX_LENGTH + 1
        
        left, right = 0, cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            if self.binaryMatrix.get(row, mid) == 1:
                leftmost_column_with_one = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return leftmost_column_with_one
